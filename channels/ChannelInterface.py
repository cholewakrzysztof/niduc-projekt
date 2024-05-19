from abc import abstractmethod
from numpy import ndarray

from coders.CoderInterface import CoderInterface
from common.RawBitChain import RawBitChain


class ChannelInterface:
    @abstractmethod
    def transmit(self, coder: CoderInterface, packet: RawBitChain) -> RawBitChain:
        pass

    @abstractmethod
    def get_encoded(self) -> RawBitChain:
        pass

