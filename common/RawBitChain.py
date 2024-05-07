import numpy


class RawBitChain:
    chain: numpy.ndarray

    def __init__(self, chain: numpy.ndarray):
        self.chain = chain

    def get_bits(self):
        return self.chain
