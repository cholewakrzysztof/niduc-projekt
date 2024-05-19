import komm
from komm import BinarySymmetricChannel
from numpy import ndarray

from channels.ChannelInterface import ChannelInterface
from coders.CoderInterface import CoderInterface


class BSCChannel(ChannelInterface):
    channel: BinarySymmetricChannel
    encoded: []

    def __init__(self, error_probability):
        self.channel = komm.BinarySymmetricChannel(error_probability)
        self.encoded = []

    def __str__(self):
        return "BSCChannel"

    def transmit(self, coder: CoderInterface, array: ndarray) -> ndarray:
        encoded_data = coder.encode(array)
        self.encoded.append(encoded_data)
        after_transmission = self.channel(encoded_data)
        return coder.decode(after_transmission)

    def get_encoded(self) -> ndarray:
        return self.encoded
