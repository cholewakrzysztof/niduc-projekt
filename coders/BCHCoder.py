import komm
from numpy import ndarray

from coders.CoderInterface import CoderInterface


class BCHCoder(CoderInterface):
    mu: int
    delta: int

    def __init__(self, mu, delta):
        self.mu = mu
        self.delta = delta

    def __str__(self):
        return "BCHCoder"

    def encode(self, array) -> ndarray:
        bch = komm.BCHCode(self.mu, self.delta)
        encoder = komm.BlockEncoder(bch)
        encoded_data = encoder(array)
        return encoded_data

    def decode(self, array: ndarray) -> ndarray:
        bch = komm.BCHCode(self.mu, self.delta)
        decoder = komm.BlockDecoder(bch)
        decoder_data = decoder(array)
        return decoder_data
