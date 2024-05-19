import csv
import datetime
import random

import komm
import numpy

import TransmissionController
from DataAnalyzer import DataAnalyzer
from DataWriter import DataWriter
from channels.BSCChannel import BSCChannel
from channels.GilbertElliottChannel import GilbertElliottChannel
from coders.BCHCoder import BCHCoder
from coders.HammingCode import HammingCode
from coders.ReedSolomonCoder import ReedSolomonCoder
from coders.SingleParityCheckCode import SingleParityCheckCode
from data.DataGenerator import DataGenerator

# Dane wejściowe
message_size = 64
#message = DataGenerator.random_bits_array_generator(message_size)
packet_size = 8
#packets = DataSequencer.divide_into_subsequences(message, packet_size)

data_generator = DataGenerator()
data_generator.generate_data(message_size, packet_size)
packets = data_generator.get_packets()

print(packets)

data_analyzer = DataAnalyzer()
data_writer = DataWriter()

error_probability = 0.1
channel = BSCChannel(error_probability)

mu = 3
delta = 7
coder = BCHCoder(mu, delta)

transmission_controller = TransmissionController.TransmissionController()
transmission_controller.set_channel(channel)
transmission_controller.set_coder(coder)
transmission_controller.set_input(packets)

transmission_controller.start_transmission()


data_analyzer.get_transmission_data(transmission_controller.get_transmission_data())

data_writer.save_to_file(data_analyzer.get_report(),"test1")


mu = 3
coder = HammingCode(mu)
#test_coder(message_size, coder, channel, packets, writer)

n = packet_size + 1
coder = SingleParityCheckCode(n)
#test_coder(message_size, coder, channel, packets, writer)

p = 0.1  # Prawdopodobieństwo przejścia ze stanu dobrego do złego
r = 0.2  # Prawdopodobieństwo przejścia ze stanu złego do dobrego
k = 0.9  # Prawdopodobieństwo poprawnej transmisji w stanie dobrym
h = 0.1  # Prawdopodobieństwo poprawnej transmisji w stanie złym
channel = GilbertElliottChannel(p, r, k, h)

n = packet_size + 3
k = packet_size
coder = ReedSolomonCoder(n, k)
#test_coder(message_size, coder, channel, packets, writer)




