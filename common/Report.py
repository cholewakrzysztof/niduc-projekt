from channels.ChannelInterface import ChannelInterface
from coders.CoderInterface import CoderInterface
from common.TestResult import TestResult


class Report:
    test_results: list[TestResult]
    coder: str
    channel: str
    message_size: int
    packet_size: int
    error_bit_rate: float
    redundancy: int

    def __init__(self,
                 test_results: list[TestResult],
                 coder: str,
                 channel: str,
                 message_size: int,
                 packet_size: int,
                 error_bit_rate: float,
                 redundancy:int):
        self.test_results = test_results
        self.coder = coder
        self.channel = channel
        self.message_size = message_size
        self.packet_size = packet_size
        self.error_bit_rate = error_bit_rate
        self.redundancy = redundancy
