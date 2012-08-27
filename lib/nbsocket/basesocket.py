# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## Clean and lightweight non-blocking socket I/O implementation
##----------------------------------------------------------------------
## Copyright (C) 2007-2011 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------

## Python modules
from __future__ import with_statement
import socket
import time
import logging
## NOC modules
from noc.lib.nbsocket.exceptions import *


class Socket(object):
    """
    Abstract non-blocking socket wrapper
    """
    TTL = None  # maximum time to live in seconds
    READ_CHUNK = 65536  # @todo: configuration parameter

    def __init__(self, factory, socket=None):
        self.factory = factory
        self.socket = socket
        self.start_time = time.time()
        self.last_read = self.start_time + 100  # @todo: Meaningful value
        self.name = None
        self.closing = False  # In closing state
        self.stale = False  # Closed as stale
        self.ttl = self.TTL
        self.set_timeout(self.TTL)
        self.factory.register_socket(self)
        if socket:
            self.set_status(r=True)

    def __repr__(self):
        return "<%s(0x%x)>" % (self.__class__.__name__, id(self))

    def create_socket(self):
        """
        Performs actial socket creation and initialization
        and pust socket into nonblocking mode.
        """
        if not self.socket_is_ready():  # Socket was not created
            raise SocketNotImplemented()
        self.socket.setblocking(0)
        self.set_status(r=True)
        self.update_status()

    def set_timeout(self, ttl):
        """
        Change socket timeout

        :param ttl: Timeout in seconds
        :type ttl: int
        """
        if ttl and ttl != self.ttl:
            self.debug("Set timeout to %s secs" % ttl)
            self.ttl = ttl

    def socket_is_ready(self):
        """
        Check socket is created and ready for operation

        :rtype: bool
        """
        return self.socket is not None

    def fileno(self):
        """
        Get socket system file id

        :return: file id or None
        :rtype: int or None
        """
        return self.socket.fileno() if self.socket else None

    def handle_read(self):
        """
        Read handler. Called every time when socket has data available
        to be reading.
        """
        pass

    def handle_write(self):
        """
        Read handler. Called every time when socket has data available
        to be written.
        """
        pass

    def on_close(self):
        """
        Close handler. Called on socket close.
        """
        pass

    def on_error(self, exc):
        """
        Error handler. Called on eny socket error.
        Default behavior is to emit error message and close the socket

        :param exc: SocketException
        """
        self.error(exc.message)
        self.close()

    def close(self):
        """
        Close socket and unregister from factory
        """
        if self.closing:
            return
        self.closing = True
        if self.socket:
            self.set_status(r=False, w=False)
            self.factory.unregister_socket(self)
            try:
                if self.socket:
                    self.socket.close()  # Can raise EBADF/EINTR
            except socket.error, why:
                pass
            self.socket = None
            self.on_close()

    def log_label(self):
        """
        Returns a prefix for log messages

        :rtype: str
        """
        return "%s(0x%x)" % (self.__class__.__name__, id(self))

    def debug(self, msg):
        """
        Emit debug-level log message.

        :param msg: Message
        :type msg: str
        """
        logging.debug("[%s] %s" % (self.log_label(), msg))

    def info(self, msg):
        """
        Emit info-level log message.

        :param msg: Message
        :type msg: str
        """
        logging.info("[%s] %s" % (self.log_label(), msg))

    def error(self, msg):
        """
        Emit error-level log message.

        :param msg: Message
        :type msg: str
        """

        logging.error("[%s] %s" % (self.log_label(), msg))

    def set_name(self, name):
        """
        Set socket name.

        :param name: Name
        :type name: str
        """
        self.name = name
        self.factory.register_socket(self, name)

    def update_status(self):
        """
        Update socket status to indicate socket still active
        """
        self.last_read = time.time()

    def set_status(self, r=None, w=None):
        self.factory.set_status(self, r=r, w=w)

    def is_stale(self):
        """
        Check socket is stale.
        Called by SocketFactory.close_stale to determine
        should socket be closed forcefully

        :rtype: bool
        """
        return (self.socket_is_ready() and self.ttl
                and time.time() - self.last_read >= self.ttl)
