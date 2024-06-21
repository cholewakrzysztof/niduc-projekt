import numpy


class DataComparator:
    @staticmethod
    def are_equal(arr1: numpy.ndarray, arr2: numpy.ndarray) -> bool:
        return numpy.array_equal(arr1, arr2)

    @staticmethod
    def count_different_elements(arr1, arr2):
        try:
            return numpy.sum(arr1 != arr2)
        except:
            print(arr1)
            print(arr2)
