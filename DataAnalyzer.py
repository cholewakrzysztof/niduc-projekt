import numpy

from DataWriter import DataWriter
from common.NumUtils import NumUtils
from common.RawBitChain import RawBitChain
from common.Report import Report
from common.TestResult import TestResult, ErrorTypes
from common.TranssmisionData import TranssmisionData
from data.DataComparator import DataComparator


class DataAnalyzer:
    test_results: list[TestResult] = []
    report: Report
    total_differences: int = 0


    def get_transmission_data(self, data: TranssmisionData):
        self.total_differences = 0

        for idx in range(len(data.in_packets)):
            input_bits = data.in_packets[idx].chain
            output_bits = data.out_packets[idx].chain
            channel_bits = data.channel_packets[idx].chain
            self.add_test_data(input_bits, output_bits, channel_bits)

        error_bit_rate = NumUtils.calculate_percentage(self.total_differences, data.message_size)

        self.report = Report(self.test_results,
                             data.coder,
                             data.channel,
                             data.message_size,
                             data.packet_size,
                             error_bit_rate)

    def add_test_data(self,
                      in_bits: numpy.ndarray,
                      out_bits: numpy.ndarray,
                      channel_bits: numpy.ndarray):
        test_result = DataAnalyzer.analyze_test_data(self, in_bits, out_bits, channel_bits)
        self.test_results.append(test_result)

    def analyze_test_data(self,
                          in_bits: numpy.ndarray,
                          out_bits: numpy.ndarray,
                          channel_bits: numpy.ndarray):
        redundancy_bits_count = len(channel_bits) - len(in_bits)

        error_type = ErrorTypes.NONE
        differences = DataComparator.count_different_elements(in_bits, out_bits)
        self.total_differences += differences

        return TestResult(in_bits,
                          out_bits,
                          len(in_bits),
                          redundancy_bits_count,
                          error_type,
                          differences)

    def get_report(self):
        return self.report


