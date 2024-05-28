import numpy


class RawBitChain:
    chain: []

    def __init__(self, chain: numpy.ndarray):
        self.chain = chain
