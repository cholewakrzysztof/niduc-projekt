import numpy as np
from numpy.random import choice
from channels.ChannelInterface import ChannelInterface
from coders.CoderInterface import CoderInterface
from common.RawBitChain import RawBitChain


class GilbertElliottChannel(ChannelInterface):

    encoded: RawBitChain

    def __init__(self, p, r, k, h):
        self.p = p  # Prawdopodobieństwo przejścia ze stanu dobrego do złego
        self.r = r  # Prawdopodobieństwo przejścia ze stanu złego do dobrego
        self.k = k  # Prawdopodobieństwo poprawnej transmisji w stanie dobrym
        self.h = h  # Prawdopodobieństwo poprawnej transmisji w stanie złym
        self.state = 'G'  # Początkowy stan kanału (dobry)

    def __str__(self):
        return "GilbertElliottChannel"

    def transmit(self, coder: CoderInterface, packet: RawBitChain) -> RawBitChain:
        self.encoded = RawBitChain(coder.encode(packet.chain))
        after_transmission = self.encoded
        for i, bit in enumerate(after_transmission.chain):
            if self.state == 'G':
                error_prob = 1 - self.k  # Prawdopodobieństwo błędu w stanie dobrym
            else:
                error_prob = 1 - self.h  # Prawdopodobieństwo błędu w stanie złym

            if choice([True, False], p=[error_prob, 1 - error_prob]):
                # Błąd wystąpił
                after_transmission.chain[i] = 1 - bit  # Odwracamy bit
            else:
                after_transmission.chain[i] = bit

            # Aktualizacja stanu kanału
            if self.state == 'G':
                if choice([True, False], p=[self.p, 1 - self.p]):
                    self.state = 'B'  # Przejście do stanu złego
            else:
                if choice([True, False], p=[self.r, 1 - self.r]):
                    self.state = 'G'  # Przejście do stanu dobrego

        result = coder.decode(after_transmission.chain)
        return RawBitChain(result)

    def get_encoded(self) -> RawBitChain:
        return self.encoded
