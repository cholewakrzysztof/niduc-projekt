from json import decoder

from komm import BlockDecoder
from komm import BlockEncoder
from komm import BCHCode
from komm import BinarySymmetricChannel
import numpy

from common import RawBitChain
import komm

class TransmissionController:  # Start of class definition

    #Properties
    bch: BCHCode
    decoder: BlockDecoder
    encoder: BlockEncoder
    channel: BinarySymmetricChannel
    InBits: list[int]
    OutBits: numpy.ndarray

    def __init__(self, mu, delta, error_probability):  # Constructor
        self.bch = komm.BCHCode(mu, delta)
        self.decoder = komm.BlockDecoder(self.bch)
        self.encoder = komm.BlockEncoder(self.bch)
        self.channel = komm.BinarySymmetricChannel(error_probability)
        self.InBits = []

    def __str__(self):
        return f'TransmissionController object'

    def receive_data(self, chain: RawBitChain):
        self.InBits = chain.get_bits()

    def start_transmission(self):
        encoded_data = self.encoder(self.InBits)
        after_transmission = self.channel(encoded_data)
        self.OutBits = self.decoder(after_transmission)

    def get_output(self):
        return self.OutBits

    def get_input(self):
        return self.InBits
