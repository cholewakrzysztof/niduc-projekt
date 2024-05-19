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


def test_transmission(channel_, coder_f, message_size_, packet_size_):
    data_generator = DataGenerator()
    data_generator.generate_data(message_size_, packet_size_)
    packets = data_generator.get_packets()

    controller = TransmissionController.TransmissionController()
    controller.set_channel(channel_)
    controller.set_coder(coder_f)
    controller.set_input(packets)
    controller.start_transmission()

    data_analyzer = DataAnalyzer()
    data_analyzer.get_transmission_data(controller.get_transmission_data())

    data_writer = DataWriter()
    data_writer.save_to_file(data_analyzer.get_report(), "test1")


message_size = 64
packet_size = 8

error_probability = 0.1
channel = BSCChannel(error_probability)

mu = 3
delta = 7
coder = BCHCoder(mu, delta)
test_transmission(channel, coder, message_size, packet_size)

mu = 3
coder = HammingCode(mu)
test_transmission(channel, coder, message_size, packet_size)

n = packet_size + 1
coder = SingleParityCheckCode(n)
test_transmission(channel, coder, message_size, packet_size)

p = 0.1  # Prawdopodobieństwo przejścia ze stanu dobrego do złego
r = 0.2  # Prawdopodobieństwo przejścia ze stanu złego do dobrego
k = 0.9  # Prawdopodobieństwo poprawnej transmisji w stanie dobrym
h = 0.1  # Prawdopodobieństwo poprawnej transmisji w stanie złym
channel = GilbertElliottChannel(p, r, k, h)
n = packet_size + 3
k = packet_size
coder = ReedSolomonCoder(n, k)
test_transmission(channel, coder, message_size, packet_size)
