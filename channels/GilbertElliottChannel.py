import numpy as np
from numpy.random import choice

from channels.ChannelInterface import ChannelInterface
from coders.CoderInterface import CoderInterface


class GilbertElliottChannel(ChannelInterface):
    def __init__(self, p, r, k, h):
        self.p = p  # Prawdopodobieństwo przejścia ze stanu dobrego do złego
        self.r = r  # Prawdopodobieństwo przejścia ze stanu złego do dobrego
        self.k = k  # Prawdopodobieństwo poprawnej transmisji w stanie dobrym
        self.h = h  # Prawdopodobieństwo poprawnej transmisji w stanie złym
        self.state = 'G'  # Początkowy stan kanału (dobry)

    def __str__(self):
        return "GilbertElliottChannel"

    def transmit(self, coder: CoderInterface, array: np.ndarray) -> np.ndarray:
        transmitted_array = np.zeros_like(array)
        for i, bit in enumerate(array):
            if self.state == 'G':
                error_prob = 1 - self.k  # Prawdopodobieństwo błędu w stanie dobrym
            else:
                error_prob = 1 - self.h  # Prawdopodobieństwo błędu w stanie złym

            if choice([True, False], p=[error_prob, 1 - error_prob]):
                # Błąd wystąpił
                transmitted_array[i] = 1 - bit  # Odwracamy bit
            else:
                transmitted_array[i] = bit

            # Aktualizacja stanu kanału
            if self.state == 'G':
                if choice([True, False], p=[self.p, 1 - self.p]):
                    self.state = 'B'  # Przejście do stanu złego
            else:
                if choice([True, False], p=[self.r, 1 - self.r]):
                    self.state = 'G'  # Przejście do stanu dobrego

        return transmitted_array
