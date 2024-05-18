import komm
from komm import BinarySymmetricChannel
from numpy import ndarray

from channels.ChannelInterface import ChannelInterface
from coders.CoderInterface import CoderInterface


class BSCChannel(ChannelInterface):
    channel: BinarySymmetricChannel

    def __init__(self, error_probability):
        self.channel = komm.BinarySymmetricChannel(error_probability)

    def __str__(self):
        return "BSCChannel"

    def transmit(self, coder: CoderInterface, array: ndarray) -> ndarray:
        encoded_data = coder.encode(array)
        after_transmission = self.channel(encoded_data)
        return coder.decode(after_transmission)
