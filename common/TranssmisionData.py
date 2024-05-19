import numpy

from channels.ChannelInterface import ChannelInterface
from coders.CoderInterface import CoderInterface


class TranssmisionData(object):
    in_bits: list[numpy.ndarray]
    out_bits: list[numpy.ndarray]
    channel_bits: list[numpy.ndarray]
    channel: ChannelInterface
    coder: CoderInterface
    packet_size: int
    message_size: int

    def __init__(self,
                 in_b: [],
                 out_b: [],
                 channel_b: [],
                 channel: ChannelInterface,
                 coder: CoderInterface,
                 packet_size: int,
                 message_size: int):
        self.in_bits = in_b
        self.out_bits = out_b
        self.channel_bits = channel_b
        self.channel = channel
        self.coder = coder
        self.packet_size = packet_size
        self.message_size = message_size
