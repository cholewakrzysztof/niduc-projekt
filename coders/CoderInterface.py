from abc import ABC, abstractmethod

from numpy import ndarray


class CoderInterface(ABC):

    @abstractmethod
    def encode(self, array) -> ndarray:
        pass

    @abstractmethod
    def decode(self, array: ndarray) -> ndarray:
        pass
