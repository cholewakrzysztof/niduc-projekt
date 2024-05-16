from abc import ABC, abstractmethod
import numpy as np
from numpy import ndarray
from reedsolo import RSCodec

from coders.CoderInterface import CoderInterface


class ReedSolomonCoder(CoderInterface):
    n: int  # dlugość całkowita bloku kodu
    k: int  # liczba bitów informacyjnych

    def __init__(self, n, k):
        self.rs = RSCodec(n - k)

    def __str__(self):
        return "ReedSolomonCoder"

    def encode(self, array) -> ndarray:
        encoded_data = self.rs.encode(array)
        return np.array(encoded_data)

    def decode(self, array: ndarray) -> ndarray:
        decoded_data = self.rs.decode(array)
        return np.array(decoded_data)
