from abc import abstractmethod
from numpy import ndarray

from coders.CoderInterface import CoderInterface


class ChannelInterface:
    @abstractmethod
    def transmit(self, coder: CoderInterface, array: ndarray) -> ndarray:
        pass

    @abstractmethod
    def get_encoded(self) -> ndarray:
        pass

