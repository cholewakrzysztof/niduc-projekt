import numpy

from DataWriter import DataWriter
from common.Report import Report
from common.TestResult import TestResult, ErrorTypes


class DataAnalyzer:
    test_results: list[TestResult] = []

    def add_test_data(self, length: int, in_bits: numpy.ndarray, out_bits: numpy.ndarray):
        test_result = DataAnalyzer.analyze_test_data(length, in_bits, out_bits)
        self.test_results.append(test_result)

    def save_report(self, file_name):
        report = Report(self.test_results)
        DataWriter.save_to_file(report, file_name)

    @staticmethod
    def analyze_test_data(length, in_bits, out_bits):
        redundancy_bits_count = 0
        error_type = ErrorTypes.NONE
        return TestResult(in_bits, out_bits,  length, redundancy_bits_count, error_type)
