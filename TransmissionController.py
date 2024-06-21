from channels.BSCChannel import BSCChannel
from channels.ChannelInterface import ChannelInterface
from coders.BCHCoder import BCHCoder
from coders.CoderInterface import CoderInterface
from coders.HammingCode import HammingCode
from common.RawBitChain import RawBitChain
from common.TransmissionData import TransmissionData


class TransmissionController:  # Start of class definition

    # Properties
    channel: ChannelInterface
    coder: CoderInterface

    input_packets: list[RawBitChain]
    output_packets: list[RawBitChain]
    channel_packets: list[RawBitChain]

    packet_size: int
    message_size: int

    def __init__(self, channel: ChannelInterface = BSCChannel, coder: CoderInterface = BCHCoder):
        self.channel = channel
        self.coder = coder
        self.channel_packets = []
        self.output_packets = []
        self.input_packets = []

    def clear(self):
        self.channel_packets = []
        self.output_packets = []
        self.input_packets = []

    def set_coder(self, coder: CoderInterface):
        self.coder = coder

    def set_channel(self, channel: ChannelInterface):
        self.channel = channel

    def __str__(self):
        return f'TransmissionController with channel: {self.channel} and coder: {self.coder}'

    def start_transmission(self):
        for packet in self.input_packets:
            received_packet = self.channel.transmit(self.coder, packet)
            self.channel_packets.append(self.channel.get_encoded())
            self.output_packets.append(received_packet)

    def get_transmission_data(self):
        if self.coder.__str__() == "BCHCoder":
            return TransmissionData(self.input_packets,
                                    self.output_packets,
                                    self.channel_packets,
                                    str(self.channel),
                                    str(self.coder),
                                    self.packet_size,
                                    self.message_size,
                                    self.coder.mu,
                                    self.coder.delta)
        elif self.coder.__str__() == "HammingCoder":
            return TransmissionData(self.input_packets,
                                    self.output_packets,
                                    self.channel_packets,
                                    str(self.channel),
                                    str(self.coder),
                                    self.packet_size,
                                    self.message_size,
                                    self.coder.mu)
        else:
            return TransmissionData(self.input_packets,
                                    self.output_packets,
                                    self.channel_packets,
                                    str(self.channel),
                                    str(self.coder),
                                    self.packet_size,
                                    self.message_size)
    def set_packets(self, packets: list[RawBitChain]):
        self.input_packets = []
        self.input_packets = packets
        self.packet_size = len(packets[0].chain)
        self.message_size = len(packets) * self.packet_size

    def set_packet(self, packet: RawBitChain):
        self.input_packets = []
        self.input_packets.append(packet)
        self.packet_size = len(packet.chain)
        self.message_size = len(packet.chain) * self.packet_size

    def get_input_packets(self):
        return self.input_packets

    def get_channel_bits(self):
        return self.channel_packets
