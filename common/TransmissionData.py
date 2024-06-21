from common.RawBitChain import RawBitChain


class TransmissionData(object):
    in_packets: list[RawBitChain] = []
    out_packets: list[RawBitChain] = []
    channel_packets: list[RawBitChain] = []
    channel: str
    coder: str
    packet_size: int
    message_size: int
    mu: int = 0
    delta:int = 0

    def __init__(self,
                 in_packets: list[RawBitChain],
                 out_packets: list[RawBitChain],
                 channel_packets: list[RawBitChain],
                 channel: str,
                 coder: str,
                 packet_size: int,
                 message_size: int,
                 mu = 0,
                 delta = 0):
        self.in_packets = in_packets
        self.out_packets = out_packets
        self.channel_packets = channel_packets
        self.channel = channel
        self.coder = coder
        self.packet_size = packet_size
        self.message_size = message_size
        self.mu = mu
        self.delta = delta
