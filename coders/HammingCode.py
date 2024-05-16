import komm
from numpy import ndarray

from coders.CoderInterface import CoderInterface

class HammingCode(CoderInterface):
    mu = 3

    def __init__(self, mu):
        self.mu = mu

    def __str__(self):
        return "HammingCoder"

    def encode(self, array) -> ndarray:
        hamm = komm.HammingCode(self.mu)
        encoder = komm.BlockEncoder(hamm)
        encoded_data = encoder(array)
        return encoded_data

    def decode(self, array: ndarray) -> ndarray:
        hamm = komm.HammingCode(self.mu)
        decoder = komm.BlockDecoder(hamm)
        decoder_data = decoder(array)
        return decoder_data