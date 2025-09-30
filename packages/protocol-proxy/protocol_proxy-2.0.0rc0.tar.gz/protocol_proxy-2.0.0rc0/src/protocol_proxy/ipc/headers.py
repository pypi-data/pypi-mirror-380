import abc
import logging
import struct

from uuid import UUID

_log = logging.getLogger(__name__)


class ProtocolHeaders:
    #  The endian_indicator and version number are added where needed and not included in the portion of the format here.
    FORMAT = 'Q32sH16s16s'
    HEADER_LENGTH = struct.calcsize(FORMAT)
    VERSION = 0                                     # 2 byte (16 bit) integer (H)

    @abc.abstractmethod
    def __init__(self, data_length: int, method_name: str, request_id: int, sender_id, sender_token, **kwargs):
        if kwargs:
            _log.warning(f'Received extra kwargs for Proxy Protocol version {self.VERSION}: {list(kwargs.keys())}')
        self.data_length: int = data_length         # 8 byte (64 bit) integer (Q)
        self.method_name: str = method_name         # 32-byte (32 character) string (32s)
        self.request_id: int = request_id           #  2-byte (16 bit) integer (H)
        self.sender_id = sender_id                  # 16-byte UUID (16s)
        self.sender_token = sender_token            # 16-byte UUID (16s)
        # TODO: The token, and possibly sender_id should be an actual encrypted token based on those values, not plain text.

    @staticmethod
    def bitflag_is_set(bit_position, byte_value):
        return bool((byte_value & (1 << bit_position)) >> bit_position)

    @abc.abstractmethod
    def pack(self):
        # TODO: The sender_id is currently the proxy_id, which is a tuple. This should probably become a UUID?
        #  (Need to figure out how/where to map one to the other.)
        return struct.pack(f'>H{ProtocolHeaders.FORMAT}', self.VERSION, self.data_length,
                           self.method_name.encode('utf8'), self.request_id, self.sender_id.bytes,
                           self.sender_token.bytes)

    @abc.abstractmethod
    def unpack(self, header_bytes):
        pass

    def __repr__(self):
        return f'ProtocolHeaders(FORMAT={self.FORMAT}, VERISON={self.VERSION},' \
               f'data_length={self.data_length}, method_name={self.method_name},' \
               f' request_id={self.request_id}, sender_id={self.sender_id}, sender_token={self.sender_token}'


class HeadersV1(ProtocolHeaders):
    FORMAT = ProtocolHeaders.FORMAT + 'H'
    HEADER_LENGTH = struct.calcsize(FORMAT)  # TODO: Should we make this a property instead?
    RESPONSE_EXPECTED_BIT = 0
    VERSION = 1

    def __init__(self, data_length: int, method_name: str, request_id: int, sender_id, sender_token,
                 response_expected: bool = False, **kwargs):
        super(HeadersV1, self).__init__(data_length, method_name, request_id, sender_id, sender_token, **kwargs)
        self.response_expected: bool = response_expected  # Position 0 in bitflags within struct.

    def pack(self):
        bitflags = (int(self.response_expected) << self.RESPONSE_EXPECTED_BIT)  # 2 byte (16-bit) bitflags.
        return super(HeadersV1, self).pack() + struct.pack(f'>H', bitflags)

    @classmethod
    def unpack(cls, header_bytes):
        (data_length, method_bytes, request_id, sender_id_bytes, sender_token_bytes,
         bitflags) = struct.unpack('>' + cls.FORMAT, header_bytes)
        response_expected = cls.bitflag_is_set(cls.RESPONSE_EXPECTED_BIT, bitflags)
        method = method_bytes.rstrip(b'\x00').decode('utf8')
        # sender_id_decoded = sender_id_bytes.rstrip(b'\x00').decode('utf8')
        # # TODO: Instead of converting back to a tuple, like this,
        # #  we should probably be using a UUID in place of proxy_id over the wire.
        # sender_id = literal_eval(sender_id_decoded)
        sender_id = UUID(bytes=sender_id_bytes)
        sender_token = UUID(bytes=sender_token_bytes)
        return cls(data_length, method, request_id, sender_id, sender_token, response_expected)
