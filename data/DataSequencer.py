import numpy


class DataSequencer:
    @staticmethod
    def divide_into_subsequences(array: numpy.ndarray, sub_size: int):
        sub_counts = len(array) // sub_size
        return numpy.array_split(array, sub_counts)
