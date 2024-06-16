import Menu
from TransmissionController import TransmissionController
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

def simulation():
    writer = DataWriter()
    writer.open('dobry_kanal', "C:\\Users\\Admin\\Desktop\\NIDUC\\")

    for iteration in range(1):
        sizes = [8,32,128]
        mu =    [2,3,3,4, 5, 6]
        delta = [3,3,7,15,31,63]
        reedSolomonRedundancies = [4,16,64,120]

        print("Generuje kodery\n")
        coders = [NoCoder(), HammingCode(2), HammingCode(3)]
        for idx in range(mu.__len__()-1):
            coders.append(BCHCoder(mu[idx], delta[idx]))
        coders = []

        generator = DataGenerator()
        analyzer = DataAnalyzer()

        print("Wstepne obiekty wygenerowane\n")

        for size in sizes:
            print(f'Generuje dane dla rozmiaru {size}\n')
            generator.generate_data(512, size)
            channel = BSCChannel(0.06)
            for coder in coders:
                print(f'Przesylam dane rozmiar: {size} koder: {coder}')

                if coder.__str__() == 'BCHCoder' or coder.__str__() == 'HammingCoder':
                    print(f' mu: {coder.mu}')
                    if coder.__str__() == 'BCHCoder':
                        print(f' delta: {coder.delta}')

                print('\n')
                controller = TransmissionController(channel, coder)
                controller.set_packets(generator.get_packets())
                controller.start_transmission()
                analyzer.get_transmission_data(controller.get_transmission_data())
                writer.writeReport(iteration, analyzer.get_report())
                print('Dane zapisane do pliku\n')

            coder = SingleParityCheckCode(size+1)
            print(f'Przesylam dane rozmiar: {size} koder: {coder}')

            if coder.__str__() == 'BCHCoder' or coder.__str__() == 'HammingCoder':
                print(f' mu: {coder.mu}')
                if coder.__str__() == 'BCHCoder':
                    print(f' delta: {coder.delta}')

            print('\n')
            controller = TransmissionController(channel, coder)
            controller.set_packets(generator.get_packets())
            controller.start_transmission()
            analyzer.get_transmission_data(controller.get_transmission_data())
            writer.writeReport(iteration, analyzer.get_report())
            print('Dane zapisane do pliku\n')

            for redundancy in reedSolomonRedundancies:
                n = size + redundancy
                k = size
                coder = ReedSolomonCoder(n,k)
                channel = GilbertElliottChannel(0.05,0.5,0.99,0.2)
                print(f'Przesylam dane rozmiar: {size} koder: {coder}')

                if coder.__str__() == 'BCHCoder' or coder.__str__() == 'HammingCoder':
                    print(f' mu: {coder.mu}')
                    if coder.__str__() == 'BCHCoder':
                        print(f' delta: {coder.delta}')

                print('\n')
                controller = TransmissionController(channel, coder)
                controller.set_packets(generator.get_packets())
                controller.start_transmission()
                analyzer.get_transmission_data(controller.get_transmission_data())
                writer.writeReport(iteration, analyzer.get_report())
                print('Dane zapisane do pliku\n')

        writer.close()

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
