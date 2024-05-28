import komm
from numpy import ndarray
from coders.CoderInterface import CoderInterface


class NoCoder(CoderInterface):
    def __str__(self):
        return "NoCoder"

    def encode(self, array) -> ndarray:
        return array

    def decode(self, array: ndarray) -> ndarray:
        return array
