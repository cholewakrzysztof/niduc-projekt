import numpy

from DataWriter import DataWriter
from common.RawBitChain import RawBitChain
from common.Report import Report
from common.TestResult import TestResult, ErrorTypes
from common.TranssmisionData import TranssmisionData
from data.DataComparator import DataComparator


class DataAnalyzer:
    test_results: list[TestResult] = []
    report: Report


    def get_transmission_data(self, data: TranssmisionData):
        for idx in range(len(data.in_bits)):
            input_bits = data.in_bits[idx]
            output_bits = data.out_bits[idx]
            channel_bits = data.channel_bits[idx]
            self.add_test_data(input_bits, output_bits,channel_bits)

        self.report = Report(self.test_results,
                             data.coder,
                             data.channel,
                             data.message_size,
                             data.packet_size)

    def add_test_data(self,
                      in_bits: numpy.ndarray,
                      out_bits: numpy.ndarray,
                      channel_bits: numpy.ndarray):
        test_result = DataAnalyzer.analyze_test_data(in_bits, out_bits, channel_bits)
        self.test_results.append(test_result)

    @staticmethod
    def analyze_test_data(in_bits: RawBitChain, out_bits: RawBitChain, channel_bits: RawBitChain):
        redundancy_bits_count = len(channel_bits.chain) - len(in_bits)

        error_type = ErrorTypes.NONE
        differences = DataComparator.count_different_elements(in_bits, out_bits)

        return TestResult(in_bits.chain,
                          out_bits.chain,
                          len(in_bits),
                          redundancy_bits_count,
                          error_type,
                          differences)

    def get_report(self):
        return self.report


