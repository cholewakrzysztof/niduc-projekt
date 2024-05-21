import numpy


class RawBitChain:
    chain: []

    def __init__(self, chain: numpy.ndarray):
        if isinstance(chain, str):
            self.chain = [int(char) for char in chain]
        else:
            self.chain = chain

    def get_bits(self):
        return self.chain
