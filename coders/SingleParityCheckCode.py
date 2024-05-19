import komm
from numpy import ndarray
from coders.CoderInterface import CoderInterface


class SingleParityCheckCode(CoderInterface):
    n: int

    def __init__(self, n):
        self.n = n

    def __str__(self):
        return "SingleParityCheckCode"

    def encode(self, array) -> ndarray:
        parit = komm.SingleParityCheckCode(self.n)
        encoder = komm.BlockEncoder(parit)
        encoded_data = encoder(array)
        return encoded_data

    def decode(self, array: ndarray) -> ndarray:
        parit = komm.SingleParityCheckCode(self.n)
        decoder = komm.BlockDecoder(parit)
        decoder_data = decoder(array)
        return decoder_data
