import komm
import numpy
from numpy import ndarray
from coders.CoderInterface import CoderInterface


class NoCoder(CoderInterface):
    def __str__(self):
        return "NoCoder"

    def encode(self, array) -> ndarray:
        new_arr = []
        for i in array:
            new_arr.append(i)
        return numpy.asarray(new_arr)

    def decode(self, array: ndarray) -> ndarray:
        return array
