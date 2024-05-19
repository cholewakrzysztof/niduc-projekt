from channels.ChannelInterface import ChannelInterface
from coders.CoderInterface import CoderInterface
from common.RawBitChain import RawBitChain


class TransmissionData(object):
    in_packets: list[RawBitChain] = []
    out_packets: list[RawBitChain] = []
    channel_packets: list[RawBitChain] = []
    channel: ChannelInterface
    coder: CoderInterface
    packet_size: int
    message_size: int

    def __init__(self,
                 in_packets: list[RawBitChain],
                 out_packets: list[RawBitChain],
                 channel_packets: list[RawBitChain],
                 channel: ChannelInterface,
                 coder: CoderInterface,
                 packet_size: int,
                 message_size: int):
        self.in_packets = in_packets
        self.out_packets = out_packets
        self.channel_packets = channel_packets
        self.channel = channel
        self.coder = coder
        self.packet_size = packet_size
        self.message_size = message_size
