import numpy as np
from numpy import ndarray
from reedsolo import RSCodec
from coders.CoderInterface import CoderInterface


class ReedSolomonCoder(CoderInterface):
    n: int  # dlugość całkowita bloku kodu
    k: int  # liczba bitów informacyjnych

    def __init__(self, n, k):
        self.rs = RSCodec(n - k)
        self.n = n
        self.k = k

    def __str__(self):
        return "ReedSolomonCoder"

    def encode(self, array) -> ndarray:
        encoded_data = self.rs.encode(array)
        return np.array(encoded_data)

    def decode(self, array: ndarray) -> ndarray:
        try:
            x, decoded_data,another = self.rs.decode(array)
        except:
            decoded_data = array

        decoded_data = decoded_data[:-(self.n-self.k)]
        return np.array([b for b in decoded_data])
