import komm
from komm import BinarySymmetricChannel
from channels.ChannelInterface import ChannelInterface
from coders.CoderInterface import CoderInterface
from common.RawBitChain import RawBitChain


class BSCChannel(ChannelInterface):
    channel: BinarySymmetricChannel
    encoded: RawBitChain

    def __init__(self, error_probability):
        self.channel = komm.BinarySymmetricChannel(error_probability)

    def __str__(self):
        return "BSCChannel"

    def transmit(self, coder: CoderInterface, packet: RawBitChain) -> RawBitChain:
        encoded_data = coder.encode(packet.chain)
        self.encoded = RawBitChain(encoded_data)
        after_transmission = self.channel(encoded_data)
        return RawBitChain(coder.decode(after_transmission))

    def get_encoded(self) -> RawBitChain:
        return self.encoded
