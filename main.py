import Menu
import TransmissionController
from DataAnalyzer import DataAnalyzer
from DataWriter import DataWriter
from CombinationHarvester import CombinationHarvester
from channels.BSCChannel import BSCChannel
from channels.GilbertElliottChannel import GilbertElliottChannel
from coders.BCHCoder import BCHCoder
from coders.HammingCode import HammingCode
from coders.NoCoder import NoCoder
from coders.ReedSolomonCoder import ReedSolomonCoder
from coders.SingleParityCheckCode import SingleParityCheckCode
from data.DataGenerator import DataGenerator


def test_transmission(channel_, coder_f, message_size_, packet_size_, name):
    data_generator = DataGenerator()
    data_generator.generate_data(message_size_, packet_size_)
    packets = data_generator.get_packets()
    controller = TransmissionController.TransmissionController()
    data_writer = DataWriter()
    data_writer.open(name, "C:\\Users\\Admin\\Desktop\\NIDUC\\")

    data_analyzer = DataAnalyzer()
    error_bit_rate = 0.0
    redundancy_sum = 0

    iteration_count = 50
    for i in range(iteration_count):
        controller.clear()
        controller.set_channel(channel_)
        controller.set_coder(coder_f)
        controller.set_packets(packets)
        controller.start_transmission()

        data_analyzer = DataAnalyzer()
        data_analyzer.get_transmission_data(controller.get_transmission_data())
        report = data_analyzer.get_report()
        error_bit_rate += report.error_bit_rate
        redundancy_sum += report.redundancy
        data_writer.writeReport(i + 1, report)  # f'{path}\\{name}_{timestamp_str}.csv'

    avg_redundancy = int(redundancy_sum / iteration_count)
    avg_error_bit_rate = error_bit_rate / iteration_count
    data_writer.writeSummary(data_analyzer.get_report(), avg_redundancy, avg_error_bit_rate)
    data_writer.close()


def simulation():
    harvester = CombinationHarvester([8,16,32,64,128,256,512,1024,2048], [2,3,4,5,6,7,8,9,10], range(3, 2, 1024))
    harvester.harvest()

    message_size = 64
    packet_size = 8

    error_probability = 0.3
    channel = BSCChannel(error_probability)

    mu = 3
    delta = 7
    coder = BCHCoder(mu, delta)
    if harvester.check_combination(coder, packet_size, mu, delta):
        test_transmission(channel, coder, message_size, packet_size, "bch")

    mu = 3
    coder = HammingCode(mu)
    if harvester.check_combination(coder, packet_size, mu, delta):
        test_transmission(channel, coder, message_size, packet_size, "hamming")

    n = packet_size + 1
    coder = SingleParityCheckCode(n)
    if harvester.check_combination(coder, n, mu, delta):
        test_transmission(channel, coder, message_size, packet_size, "parzystosc")

    p = 0.1  # Prawdopodobieństwo przejścia ze stanu dobrego do złego
    r = 0.2  # Prawdopodobieństwo przejścia ze stanu złego do dobrego
    k = 0.9  # Prawdopodobieństwo poprawnej transmisji w stanie dobrym
    h = 0.1  # Prawdopodobieństwo poprawnej transmisji w stanie złym
    channel = GilbertElliottChannel(p, r, k, h)
    n = packet_size + 3
    k = packet_size
    coder = ReedSolomonCoder(n, k)
    if harvester.check_combination(coder, n, mu, delta):
        test_transmission(channel, coder, message_size, packet_size, "reedsolomon")


harvester = CombinationHarvester([2048], [2,3,4,5,6,7,8], [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 69, 71, 73, 75, 77, 79, 83, 85, 87, 89, 91, 93, 95, 99, 101, 103, 105, 107, 109, 111, 115, 117, 119, 121, 123, 125, 127, 147, 149, 151, 155, 157, 159, 165, 167, 171, 173, 175, 179, 181, 183, 187, 189, 191, 205, 207, 213, 215, 219, 221, 223, 231, 235, 237, 239, 245, 247, 251, 253, 255 ])#341, 343, 347, 351, 363, 367, 375, 379, 383, 439, 447, 479, 495, 511, 1023
harvester.harvest()

into = 0
opcja = 0
while True:
    isExistBC = 'packets' in globals()
    isExistTC = 'controller' in globals()
    Menu.wyswietl_menu(isExistBC, isExistBC, into)
    wybor = Menu.wybor()
    opcja += Menu.obliczenie_opcji(into, wybor)
    if opcja == 0:
        break
    elif opcja == 900:
        simulation()
        opcja = 0
    elif opcja == 100:
        pass
    elif opcja == 200:
        pass
    elif opcja == 300:
        pass
    else:
        pass
