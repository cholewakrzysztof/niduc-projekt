import random
import numpy


class DataGeneratorAnna:
    @staticmethod
    def random_bits_array_generator(length):
        arr = [random.randint(0, 1) for i in range(0, length)]
        return numpy.array(arr)
