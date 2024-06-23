import string

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


def bsc_channel_simulation(error_prob, mus, deltas, sizes, iteration, message_size, writer, rs):
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
            print(f'    Koder: {coder} ukonczony')
        coder = SingleParityCheckCode(size + 1)
        controller = TransmissionController(channel, coder)
        controller.set_packets(generator.get_packets())
        controller.start_transmission()
        analyzer.get_transmission_data(controller.get_transmission_data())
        writer.writeReport(iteration, analyzer.get_report())
        print(f'Rozmiar {size} ukonczony')


def gilbert_eliot_simulation(p, r, k, h, sizes, iteration, message_size, writer, rs):
    reed_solomon_redundancies = rs

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
            print(f'    Nadmiarowosc {redundancy} ukonczona')

        coder = NoCoder()
        channel = GilbertElliottChannel(p, r, k, h)
        controller = TransmissionController(channel, coder)
        controller.set_packets(generator.get_packets())
        controller.start_transmission()
        analyzer.get_transmission_data(controller.get_transmission_data())
        writer.writeReport(iteration, analyzer.get_report())
        print(f'Rozmiar {size} ukonczony')


def simulation(path: string, name: string, sizes: list, mu: list, delta: list, message_size, iterations, rs: list):

    writerd = DataWriter()
    writerd.open(f'{name}_good', path)

    er_p = input('Podaj prawdopodobieństwo błędu dla kanału dobrej jakości (pozostaw puste dla wartości domyślnej):')
    error_p = eval(er_p) if er_p.__len__() > 0 else 0.06

    ps = input('Podaj prawdopodobieństwo p dla kanału dobrej jakości (pozostaw puste dla wartości domyślnej):')
    p = eval(ps) if ps.__len__() > 0 else 0.05
    r_s = input('Podaj prawdopodobieństwo r dla kanału dobrej jakości (pozostaw puste dla wartości domyślnej):')
    r = eval(r_s) if r_s.__len__() > 0 else 0.5
    ks = input('Podaj prawdopodobieństwo k dla kanału dobrej jakości (pozostaw puste dla wartości domyślnej):')
    k = eval(ks) if ks.__len__() > 0 else 0.99
    hs = input('Podaj prawdopodobieństwo h dla kanału dobrej jakości (pozostaw puste dla wartości domyślnej):')
    h = eval(hs) if hs.__len__() > 0 else 0.2

    for i in range(iterations):
        bsc_channel_simulation(error_p, mu, delta, sizes, i, message_size, writerd, rs)
        gilbert_eliot_simulation(p, r, k, h, sizes, i, message_size, writerd, rs)
        print(f'Koniec iteracji {i + 1} dla kanału dobrej jakości')
    writerd.close()

    er_p = input('Podaj prawdopodobieństwo błędu dla kanału średniej jakości (pozostaw puste dla wartości domyślnej):')
    error_p = eval(er_p) if er_p.__len__() > 0 else 0.1

    ps = input('Podaj prawdopodobieństwo p dla kanału średniej jakości (pozostaw puste dla wartości domyślnej):')
    p = eval(ps) if ps.__len__() > 0 else 0.07
    r_s = input('Podaj prawdopodobieństwo r dla kanału średniej jakości (pozostaw puste dla wartości domyślnej):')
    r = eval(r_s) if r_s.__len__() > 0 else 0.38
    ks = input('Podaj prawdopodobieństwo k dla kanału średniej jakości (pozostaw puste dla wartości domyślnej):')
    k = eval(ks) if ks.__len__() > 0 else 0.92
    hs = input('Podaj prawdopodobieństwo h dla kanału średniej jakości (pozostaw puste dla wartości domyślnej):')
    h = eval(hs) if hs.__len__() > 0 else 0.17

    writers = DataWriter()
    writers.open(f'{name}_medium', path)
    for i in range(iterations):
        bsc_channel_simulation(error_p, mu, delta, sizes, i, message_size, writers, rs)
        gilbert_eliot_simulation(p, r, k, h, sizes, i, message_size, writers, rs)
        print(f'Koniec iteracji {i + 1} dla kanału średniej jakości')
    writers.close()

    er_p = input('Podaj prawdopodobieństwo błędu dla kanału słabej jakości (pozostaw puste dla wartości domyślnej):')
    error_p = eval(er_p) if er_p.__len__() > 0 else 0.3

    ps = input('Podaj prawdopodobieństwo p dla kanału słabej jakości (pozostaw puste dla wartości domyślnej):')
    p = eval(ps) if ps.__len__() > 0 else 0.1
    r_s = input('Podaj prawdopodobieństwo r dla kanału słabej jakości (pozostaw puste dla wartości domyślnej):')
    r = eval(r_s) if r_s.__len__() > 0 else 0.31
    ks = input('Podaj prawdopodobieństwo k dla kanału słabej jakości (pozostaw puste dla wartości domyślnej):')
    k = eval(ks) if ks.__len__() > 0 else 0.87
    hs = input('Podaj prawdopodobieństwo h dla kanału słabej jakości (pozostaw puste dla wartości domyślnej):')
    h = eval(hs) if hs.__len__() > 0 else 0.12

    writerz = DataWriter()
    writerz.open(f'{name}_bad', path)
    for i in range(iterations):
        bsc_channel_simulation(error_p, mu, delta, sizes, i, message_size, writerz, rs)
        gilbert_eliot_simulation(p, r, k, h, sizes, i, message_size, writerz, rs)
        print(f'Koniec iteracji {i + 1} dla kanału słabej jakości')
    writerz.close()

print('Witamy w symulatorze FEC!')
while True:
    path = input('Wybierz ścieżkę docelową: ')
    name = input('Wybierz nazwę pliku docelowego: ')
    try:
        sizes = [eval(b) for b in input('Podaj rozmiary pakietów (x-y-z): ').split('-')]
        mu = [eval(b) for b in input('Podaj listę mu (x-y-z): ').split('-')]
        delta = [eval(b) for b in input('Podaj listę delta (x-y-z): ').split('-')]
        rs = [eval(b) for b in input('Podaj listę nadmiarowości RS (x-y-z): ').split('-')]
        message_size = eval(input('Podaj rozmiar wiadomości:'))
        iterations = eval(input('Podaj liczbę iteracji:'))
        print('Symulacja rozpoczęta...')
        try:
            simulation(path, name, sizes, mu, delta, message_size, iterations, rs)
            print('Symulacja zakończona\n\n\n')
        except:
            print('Podano błędne dane!')
    except:
        'Błędne dane wejściowe!'

    input('Naciśnij dowolny klawisz, aby rozpocząć nową symulację')
    print('\n')