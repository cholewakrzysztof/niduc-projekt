from enum import Enum
import numpy


class ErrorTypes(Enum):
    NONE = 0
    MIXED = 1
    SINGLE = 2
    GROUPED = 3


class TestResult:
    in_bits: numpy.ndarray
    out_bits: numpy.ndarray
    length: int
    redundancy_bits_count: int
    error_type: ErrorTypes
    error_appeared: bool
    differences_count: int

    def __init__(self,
                 in_bits: numpy.ndarray,
                 out_bits: numpy.ndarray,
                 length: int,
                 redundancy_bits_count: int,
                 error_type: ErrorTypes,
                 differences_count: int):
        self.in_bits = in_bits
        self.out_bits = out_bits
        self.length = length
        self.redundancy_bits_count = redundancy_bits_count
        self.error_type = error_type
        self.error_appeared = error_type != ErrorTypes.NONE
        self.differences_count = differences_count

    def as_list(self):
        return [self.in_bits.__str__(),
                self.out_bits.__str__(),
                self.length,
                self.redundancy_bits_count,
                self.error_type,
                self.error_appeared,
                self.differences_count]
