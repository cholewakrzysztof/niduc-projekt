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


def test_transmission(controller_f, channel_, coder_f, packets_f):
    controller_f.set_channel(channel_)
    controller_f.set_coder(coder_f)
    controller_f.set_input(packets_f)
    controller_f.start_transmission()
    data_analyzer.get_transmission_data(controller_f.get_transmission_data())
    data_writer.save_to_file(data_analyzer.get_report(), "test1")

# Dane wejściowe
message_size = 64
packet_size = 8

data_generator = DataGenerator()
data_generator.generate_data(message_size, packet_size)
packets = data_generator.get_packets()
controller = TransmissionController.TransmissionController()


print(packets)

data_analyzer = DataAnalyzer()
data_writer = DataWriter()

error_probability = 0.1
channel = BSCChannel(error_probability)

mu = 3
delta = 7
coder = BCHCoder(mu, delta)
test_transmission(controller, channel, coder, packets)

mu = 3
coder = HammingCode(mu)
test_transmission(controller, channel, coder, packets)

n = packet_size + 1
coder = SingleParityCheckCode(n)
test_transmission(controller, channel, coder, packets)


p = 0.1  # Prawdopodobieństwo przejścia ze stanu dobrego do złego
r = 0.2  # Prawdopodobieństwo przejścia ze stanu złego do dobrego
k = 0.9  # Prawdopodobieństwo poprawnej transmisji w stanie dobrym
h = 0.1  # Prawdopodobieństwo poprawnej transmisji w stanie złym
channel = GilbertElliottChannel(p, r, k, h)
n = packet_size + 3
k = packet_size
coder = ReedSolomonCoder(n, k)
test_transmission(controller, channel, coder, packets)
