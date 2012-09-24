# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## PingSocket implementation
##----------------------------------------------------------------------
## Copyright (C) 2007-2012 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------

## Python modules
import socket
from errno import *
import struct
import time
## NOC modules
from noc.lib.nbsocket.basesocket import Socket

ICMPv4_PROTO = socket.IPPROTO_ICMP
ICMPv4_ECHOREPLY = 0
ICMPv4_ECHO = 8
ICMPv6_PROTO = socket.IPPROTO_ICMPV6
ICMPv6_ECHO = 128
ICMPv6_ECHOREPLY = 129
MAX_RECV = 1500


class PingSocket(Socket):
    """
    Abstract ICMP Echo Request sender, Echo Reply receiver
    """
    ECHO_TYPE = None
    HEADER_SIZE = None

    def __init__(self, factory):
        # Pending pings
        self.out_buffer = []  # (address, size, count)
        # Running pings
        self.sessions = {}  # Request Id -> PingSession
        super(PingSocket, self).__init__(factory)

    def _create_socket(self):
        raise NotImplementedError

    def create_socket(self):
        self._create_socket()
        super(PingSocket, self).create_socket()
        if self.out_buffer:
            self.set_status(w=True)

    def handle_write(self):
        while self.out_buffer:
            session = self.out_buffer.pop(0)
            self.sessions[session.req_id] = session
            msg = session.build_echo_request()
            try:
                # Port is irrelevant for icmp
                self.socket.sendto(msg, (session.address, 1))
            except socket.error, why:  # ENETUNREACH
                self.debug("Socket error: %s" % why)
                session.register_miss()
                return
        self.set_status(w=bool(self.out_buffer))
        self.update_status()

    def parse_reply(self, msg, addr):
        raise NotImplementedError

    def handle_read(self):
        self.update_status()
        try:
            msg, addr = self.socket.recvfrom(MAX_RECV)
        except socket.error, why:
            if why[0] in (EINTR, EAGAIN):
                return
            raise socket.error, why
        self.parse_reply(msg, addr)

    def ping(self, addr, size=64, count=1, timeout=3, callback=None):
        """
        Start ping

        callback is a callable accepting named parameters:
            address, list of result
        :param addr:
        :param size:
        :param count:
        :param callback:
        :return:
        """
        self.out_buffer += [
            PingSession(self, address=addr, size=size,
                count=count, timeout=timeout, callback=callback)
        ]
        if self.socket:
            self.set_status(w=True)

    def get_session_class(self):
        raise NotImplementedError

    def close_session(self, session):
        if session.req_id in self.sessions:
            del self.sessions[session.req_id]

    def is_stale(self):
        """
        Timeouts handling
        """
        t = time.time()
        expired = [self.sessions[r]
                   for r in self.sessions
                   if self.sessions[r].expire and
                      self.sessions[r].expire <= t]
        for s in expired:
            s.register_miss()


class Ping4Socket(PingSocket):
    """
    ICMPv4 Ping Socket
    """
    ECHO_TYPE = ICMPv4_ECHO
    HEADER_SIZE = 28

    def _create_socket(self):
        self.socket = socket.socket(
            socket.AF_INET, socket.SOCK_RAW, ICMPv4_PROTO)

    def parse_reply(self, msg, addr):
        ip_header = msg[:20]
        (ver, tos, plen, pid, flags,
         ttl, proto, checksum, src_ip,
         dst_ip) = struct.unpack("!BBHHHBBHII", ip_header)

        icmp_header = msg[20:28]
        (icmp_type, icmp_code, icmp_checksum,
        req_id, seq) = struct.unpack(
            "!BBHHH", icmp_header)
        if icmp_type == ICMPv4_ECHOREPLY and req_id in self.sessions:
            self.sessions[req_id].register_reply(
                address=src_ip, seq=seq, ttl=ttl,
                payload=msg[self.HEADER_SIZE:])


class Ping6Socket(PingSocket):
    """
    ICMPv6 Ping Socket
    """
    ECHO_TYPE = ICMPv6_ECHO
    HEADER_SIZE = 48

    def _create_socket(self):
        self.socket = socket.socket(
            socket.AF_INET6, socket.SOCK_RAW, ICMPv6_PROTO)

    def parse_reply(self, msg, addr):
        # (ver_tc_flow, plen, hdr, ttl) = struct.unpack("!IHBB", msg[:8])
        # src_ip = msg[64: 192]
        # @todo: Access IPv6 header
        src_ip = None
        ttl = None
        # icmp_header = msg[40:48]
        icmp_header = msg[:8]
        (icmp_type, icmp_code, icmp_checksum,
         req_id, seq) = struct.unpack("!BBHHH", icmp_header)
        payload = msg[8:]
        if icmp_type == ICMPv6_ECHOREPLY and req_id in self.sessions:
            self.sessions[req_id].register_reply(
                address=src_ip, seq=seq, ttl=ttl,
                payload=payload)


class PingSession(object):
    def __init__(self, ping_socket, address, size,
                 count, timeout, callback):
        self.ping_socket = ping_socket
        self.address = address
        self.size = size
        self.count = count
        self.left = count
        self.timeout = timeout
        self.callback = callback
        self.expire = None
        self.req_id = id(self) & 0xFFFF
        self.seq = 0
        self.payload = None
        self.result = []
        self.t = None

    def register_miss(self):
        self.result += [None]
        self.next()

    def register_reply(self, address, seq, ttl, payload):
        if seq != self.seq or payload != self.payload:
            return
        # @todo: Check checksum
        t = time.time()
        # Append result
        self.result += [t - self.t]
        self.next()

    def next(self):
        """
        Process next action
        """
        self.seq += 1
        self.expire = None
        if self.seq >= self.count:
            self.ping_socket.close_session(self)
            if self.callback:
                self.callback(self.address, self.result)
        else:
            # Next round
            self.ping_socket.out_buffer += [self]
            self.ping_socket.set_status(w=True)

    def get_checksum(self, msg):
        """
        Calculate checksum
        (RFC-1071)
        """
        lm = len(msg)
        l = lm // 2
        # Calculate the sum of network-ordered shorts
        s = sum(struct.unpack("!" + "H" * l, msg[:2 * l]))
        if lm < l:
            # Add remaining octet
            s += ord(msg[-1])
        # Truncate to 32 bits
        s &= 0xFFFFFFFF
        # Fold 32 bits to 16 bits
        s = (s >> 16) + (s & 0xFFFF)  # Add high 16 bits to low 16 bits
        s += (s >> 16)
        return ~s & 0xFFFF

    def build_echo_request(self):
        checksum = 0
        self.req_id = id(self) & 0xFFFF
        # Fake header with zero checksum
        header = struct.pack("!BBHHH",
            self.ping_socket.ECHO_TYPE, 0,
            checksum, self.req_id, self.seq)
        # Pad to size
        self.payload = "A" * (self.size - self.ping_socket.HEADER_SIZE)
        # Get checksum
        checksum = self.get_checksum(header + self.payload)
        # Rebuild header with proper checksum
        header = struct.pack("!BBHHH",
            self.ping_socket.ECHO_TYPE, 0,
            checksum, self.req_id, self.seq)
        # Save time
        self.t = time.time()
        self.expire = self.t + self.timeout
        return header + self.payload
