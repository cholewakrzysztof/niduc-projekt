import csv
import datetime

from channels import ChannelInterface
from channels.BSCChannel import BSCChannel
from channels.GilbertElliottChannel import GilbertElliottChannel
from coders.BCHCoder import BCHCoder
from coders.CoderInterface import CoderInterface
from coders.HammingCode import HammingCode
from coders.ReedSolomonCoder import ReedSolomonCoder
from coders.SingleParityCheckCode import SingleParityCheckCode
from common.NumUtils import NumUtils
from data.DataComparator import DataComparator
from data.DataSequencer import DataSequencer
from data.DataGenerator import DataGenerator


def test_coder(message_size: int, coder: CoderInterface, channel: ChannelInterface, packets: list, writer):
    # global correct, packet, received, differences
    sum_differences = 0
    for packet in packets:
        received = channel.transmit(coder, packet)
        differences = DataComparator.count_different_elements(packet, received)
        sum_differences += differences
        writer.writerow([coder, channel, packet_size, packet, received, differences, ''])

    error_bit_rate = NumUtils.calculate_percentage(sum_differences, message_size)
    writer.writerow([coder, channel, packet_size, '', '', '', error_bit_rate])
    print(f"{coder};{channel};{packet_size};;;{error_bit_rate}")


message_size = 64
#message = DataGenerator.random_bits_array_generator(message_size)
packet_size = 8
#packets = DataSequencer.divide_into_subsequences(message, packet_size)

data_generator = DataGenerator()
data_generator.generate_data(message_size, packet_size)
packets = data_generator.get_packets()

current_time = datetime.datetime.now()
timestamp_str = current_time.strftime("%Y-%m-%d_%H%M%S")
file_name = f'C:\\Users\\Admin\\Desktop\\NIDUC\\_results_{timestamp_str}.csv'
file_csv = open(file_name, 'w', newline='')
writer = csv.writer(file_csv, delimiter=';')
writer.writerow(['Coder', 'Channel', 'Packet Size', 'In', 'Out', 'Differences', 'Bit error rate'])

error_probability = 0.1
channel = BSCChannel(error_probability)

mu = 3
delta = 7
coder = BCHCoder(mu, delta)
#test_coder(message_size, coder, channel, packets, writer)

mu = 3
coder = HammingCode(mu)
test_coder(message_size, coder, channel, packets, writer)

n = packet_size + 1
coder = SingleParityCheckCode(n)
test_coder(message_size, coder, channel, packets, writer)

p = 0.1  # Prawdopodobieństwo przejścia ze stanu dobrego do złego
r = 0.2  # Prawdopodobieństwo przejścia ze stanu złego do dobrego
k = 0.9  # Prawdopodobieństwo poprawnej transmisji w stanie dobrym
h = 0.1  # Prawdopodobieństwo poprawnej transmisji w stanie złym
channel = GilbertElliottChannel(p, r, k, h)

n = packet_size + 3
k = packet_size
coder = ReedSolomonCoder(n, k)
test_coder(message_size, coder, channel, packets, writer)
