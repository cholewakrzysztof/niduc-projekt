import Menu
from TransmissionController import TransmissionController
from DataAnalyzer import DataAnalyzer
from DataWriter import DataWriter
from channels.BSCChannel import BSCChannel
from channels.GilbertElliottChannel import GilbertElliottChannel
from coders.BCHCoder import BCHCoder
from coders.HammingCode import HammingCode
from coders.NoCoder import NoCoder
from coders.ReedSolomonCoder import ReedSolomonCoder
from coders.SingleParityCheckCode import SingleParityCheckCode
from data.DataGenerator import DataGenerator


def bsc_channel_simulation(error_prob, mus, deltas, sizes, iteration, message_size, writer):
    coders = [NoCoder(), HammingCode(2), HammingCode(3)]
    for idx in range(mus.__len__()):
        coders.append(BCHCoder(mus[idx], deltas[idx]))

    generator = DataGenerator()
    analyzer = DataAnalyzer()

    for size in sizes:
        generator.generate_data(message_size, size)
        channel = BSCChannel(error_prob)
        for coder in coders:
            controller = TransmissionController(channel, coder)
            controller.set_packets(generator.get_packets())
            controller.start_transmission()
            analyzer.get_transmission_data(controller.get_transmission_data())
            writer.writeReport(iteration, analyzer.get_report())
            print(f'    Coder {coder} finished')
        coder = SingleParityCheckCode(size + 1)
        controller = TransmissionController(channel, coder)
        controller.set_packets(generator.get_packets())
        controller.start_transmission()
        analyzer.get_transmission_data(controller.get_transmission_data())
        writer.writeReport(iteration, analyzer.get_report())
        print(f'Size {size} finished')


def gilbert_eliot_simulation(p, r, k, h, sizes, iteration, message_size, writer):
    reed_solomon_redundancies = [8, 16, 24, 48, 96, 112, 240]

    generator = DataGenerator()
    analyzer = DataAnalyzer()

    for size in sizes:
        generator.generate_data(message_size, size)
        for redundancy in reed_solomon_redundancies:
            n = size + redundancy
            k_n = size
            coder = ReedSolomonCoder(n, k_n)
            channel = GilbertElliottChannel(p, r, k, h)
            controller = TransmissionController(channel, coder)
            controller.set_packets(generator.get_packets())
            controller.start_transmission()
            analyzer.get_transmission_data(controller.get_transmission_data())
            writer.writeReport(iteration, analyzer.get_report())
            print(f'    Redundancy {redundancy} finished')

        coder = NoCoder()
        channel = GilbertElliottChannel(p, r, k, h)
        controller = TransmissionController(channel, coder)
        controller.set_packets(generator.get_packets())
        controller.start_transmission()
        analyzer.get_transmission_data(controller.get_transmission_data())
        writer.writeReport(iteration, analyzer.get_report())
        print(f'Size {size} finished')


def simulation():
    sizes = [8,32,128]
    mu = [2, 3, 3, 4, 5] #6
    delta = [3, 3, 7, 15, 31] #63
    path = "C:\\Users\\Admin\\Desktop\\NIDUC\\"
    message_size = 1024
    iterations = range(3)

    writerd = DataWriter()
    writerd.open(f'dobry', path)
    for i in iterations:
        bsc_channel_simulation(0.06, mu, delta, sizes, i, message_size, writerd)
        gilbert_eliot_simulation(0.05, 0.5, 0.99, 0.2, sizes, i, message_size, writerd)
        print(f'End of iteration {i} for dobry')
    writerd.close()

    writers = DataWriter()
    writers.open(f'sredni', path)
    for i in iterations:
        bsc_channel_simulation(0.25, mu, delta, sizes, i, message_size, writers)
        gilbert_eliot_simulation(0.08, 0.35, 0.9, 0.15, sizes, i, message_size, writers)
        print(f'End of iteration {i} for sredni')
    writers.close()

    writerz = DataWriter()
    writerz.open(f'zly', path)
    for i in iterations:
        bsc_channel_simulation(0.45, mu, delta, sizes, i, message_size, writerz)
        gilbert_eliot_simulation(0.12, 0.15, 0.9, 0.09, sizes, i, message_size, writerz)
        print(f'End of iteration {i} for zly')
    writerz.close()



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
