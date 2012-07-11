# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## ASN.1 BER utitities
##----------------------------------------------------------------------
## Copyright (C) 2007-2012 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------


class DecodeError(Exception):
    pass


class BERDecoder(object):
    def parse_type(self, msg):
        """
        :param msg:
        :return:  tag number, primitive flag, rest
        """
        v = ord(msg[0])
        is_primitive = not bool(v & 0x20)
        if v & 0x1f == 0x1f:
            # high-tag number form
            v = 0
            i = 1
            while True:
                c = ord(msg[i])
                i += 1
                v = v * 128 + c & 0x7f
                if not (c & 0x80):
                    break
            return v, is_primitive, msg[i:]
        else:
            # low tag number form
            return v & 0x1f, is_primitive, msg[1:]

    def parse_length(self, msg):
        v = ord(msg[0])
        if v & 0x80:
            # Long form
            l = v & 0x7f
            v = 0
            for c in msg[1:1 + l]:
                v += (v << 8) + ord(c)
            return v, msg[1 + l:]
        else:
            # Short form
            return v, msg[1:]

    def parse_tlv(self, msg):
        tag, is_primitive, msg = self.parse_type(msg)
        decoder = self.DECODERS[is_primitive].get(tag)
        length, msg = self.parse_length(msg)
        value = msg[:length]
        if decoder is None:
            pt = "primitive" if is_primitive else "constructed"
            raise DecodeError(
                "Cannot find BER decoder for %s class %d (%X)" % (
                    pt, tag, tag))
        value = decoder(self, value)
        return value, msg[length:]

    def parse_eoc(self, msg):
        return None

    def parse_boolean(self, msg):
        return bool(ord(msg[0]))

    def parse_int(self, msg):
        """
        >>> BERDecoder().parse_int('')
        0
        >>> BERDecoder().parse_int('\\x00')
        0
        >>> BERDecoder().parse_int('\\x01')
        1
        >>> BERDecoder().parse_int('\\x7f')
        127
        >>> BERDecoder().parse_int('\\x00\\x80')
        128
        >>> BERDecoder().parse_int('\\x01\\x00')
        256
        >>> BERDecoder().parse_int('\\x80')
        -128
        >>> BERDecoder().parse_int('\\xff\\x7f')
        -129

        :param msg:
        :return: integer
        """
        if not msg:
            return 0
        v = 0
        for c in msg:
            v = (v << 8) + ord(c)
        if ord(msg[0]) & 0x80:
            # Negative number
            m = 2 ** (8 * len(msg))
            v = -(m - v)
        return v

    def parse_p_bitstring(self, msg):
        unused = ord(msg[0])
        r = "".join(BITSTING[ord(c)] for c in msg)
        if unused:
            r = r[:-unused]
        return r

    def parse_p_octetstring(self, msg):
        return msg

    def parse_c_octetstring(self, msg):
        r = []
        while msg:
            v, msg = self.parse_tlv(msg)
            r += [v]
        return r

    def parse_null(self, msg):
        return None

    def parse_p_oid(self, msg):
        def parse_octet(msg):
            n = 0
            r = 0
            for c in msg:
                v = ord(c)
                r = (r << 7) + (v & 0x7f)
                n += 1
                if v < 127:
                    break
            return r, msg[n:]

        r = [c for c in divmod(ord(msg[0]), 40)]
        msg = msg[1:]
        while msg:
            v, msg = parse_octet(msg)
            r += [v]
        return ".".join("%d" % c for c in r)

    def parse_sequence(self, msg):
        r = []
        while msg:
            v, msg = self.parse_tlv(msg)
            r += [v]
        return r

    def parse_set(self, msg):
        r = []
        while msg:
            v, msg = self.parse_tlv(msg)
            r += [v]
        return r

    DECODERS = {
        # Primitive types
        True: {
            # EOC (End-of-Content)	P	0	0
            0: parse_eoc,  # 0, 0, EOC (End-of-Content)
            1: parse_boolean,  # 1, 0x1, BOOLEAN
            2: parse_int,  # 2, 0x2, INTEGER
            3: parse_p_bitstring,  # 3, 0x3, BIT STRING
            4: parse_p_octetstring,  # 4, 0x4, OCTET STRING
            5: parse_null,  # 5, 0x5, NULL
            6: parse_p_oid,  # 6, 0x6, OBJECT IDENTIFIER
            # Object Descriptor	P/C	7	7
            # EXTERNAL	C	8	8
            # REAL (float)	P	9	9
            10: parse_int,  # 10, 0xA, ENUMERATED
            # UTF8String	P/C	12	C
            # RELATIVE-OID	P	13	D
            # NumericString	P/C	18	12
            # PrintableString	P/C	19	13
            # T61String	P/C	20	14
            # VideotexString	P/C	21	15
            # IA5String	P/C	22	16
            # UTCTime	P/C	23	17
            # GeneralizedTime	P/C	24	18
            # GraphicString	P/C	25	19
            # VisibleString	P/C	26	1A
            # GeneralString	P/C	27	1B
            # UniversalString	P/C	28	1C
            # CHARACTER STRING	P/C	29	1D
            # BMPString	P/C	30	1E
            # (use long-form)	-	31	1F
        },
        # Constructed types
        False: {
            # BIT STRING	P/C	3	3
            4: parse_c_octetstring,  # 4, 0x4, OCTET STRING
            6: parse_sequence,  # 6, 0x6, OBJECT IDENTIFIER
            # Object Descriptor	P/C	7	7
            7: parse_sequence,
            # EXTERNAL	C	8	8
            # EMBEDDED PDV	C	11	B
            # UTF8String	P/C	12	C
            16: parse_sequence,  # 10, 0x10, SEQUENCE and SEQUENCE OF
            17: parse_set,  # 17, 0x11, SET and SET OF
            # NumericString	P/C	18	12
            # PrintableString	P/C	19	13
            # T61String	P/C	20	14
            # VideotexString	P/C	21	15
            # IA5String	P/C	22	16
            # UTCTime	P/C	23	17
            # GeneralizedTime	P/C	24	18
            # GraphicString	P/C	25	19
            # VisibleString	P/C	26	1A
            # GeneralString	P/C	27	1B
            # UniversalString	P/C	28	1C
            # CHARACTER STRING	P/C	29	1D
            # BMPString	P/C	30	1E
            # (use long-form)	-	31	1F
        }
    }


def decode(msg):
    decoder = BERDecoder()
    data, _ = decoder.parse_tlv(msg)
    return data

# Calculate bitsting cache
# value -> string of bits
BITSTING = {}
for i in range(256):
    BITSTING[i] = "".join(
        "%d" % ((i >> j) & 1) for j in range(7, -1, -1))
