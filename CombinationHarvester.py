from TransmissionController import TransmissionController
from channels.BSCChannel import BSCChannel
from channels.GilbertElliottChannel import GilbertElliottChannel
from coders.BCHCoder import BCHCoder
from coders.CoderInterface import CoderInterface
from coders.HammingCode import HammingCode
from coders.ReedSolomonCoder import ReedSolomonCoder
from coders.SingleParityCheckCode import SingleParityCheckCode
from common.RawBitChain import RawBitChain
from data.DataGenerator import DataGenerator


class Combination:
    channel: str
    coder: str
    combination = []

    def __init__(self, channel: str, coder: str):
        self.channel = channel
        self.coder = coder

    def __str__(self):
        return f'Channel: {self.channel}, Coder: {self.coder}, Combination (size,mu,delta): {self.combination}'


def harvest_single_combination(coder: str,
                               packet: RawBitChain,
                               mu: int = 0,
                               delta: int = 0,
                               error_probability: float = 0.1) -> Combination:

    controller = TransmissionController()

    channel = BSCChannel(error_probability)

    comb = Combination(channel.__str__(), coder)
    comb.combination = []
    comb.combination.append(len(packet.chain))

    if coder == 'BCHCoder':
        coder = BCHCoder(mu, delta)
        comb.combination.append(mu)
        comb.combination.append(delta)
    elif coder == 'HammingCoder':
        coder = HammingCode(mu)
        comb.combination.append(mu)
    elif coder == 'SingleParityCheckCode':
        coder = SingleParityCheckCode(len(packet.chain) + 1)
        comb.combination.append(len(packet.chain))
    elif coder == 'ReedSolomonCoder':
        channel = GilbertElliottChannel(0.1, 0.2, 0.9, 0.1)
        coder = ReedSolomonCoder(len(packet.chain)+3, len(packet.chain))

    controller.set_channel(channel)
    controller.set_coder(coder)
    controller.set_packet(packet)
    controller.start_transmission()
    return comb


def check_combination(coder_: CoderInterface, packet: RawBitChain) -> bool:
    coder = coder_.__str__()
    try:
        harvest_single_combination(coder, packet, 0, 0, 0.1)
        return True
    except:
        return False


class CombinationHarvester:

    coders: list[str] = ['BCHCoder', 'HammingCoder'] # , 'SingleParityCheckCode',
    channels: list[str] = ['BSCChannel']
    packet_sizes: list[int] = [8,16,32,64,128,256,512,1024,2048]
    error_prob: list[int] = [0.1]
    mu: list[int] = [2,3,4,5,6,7,8,9,10]
    delta: list[int] = [0.1]

    def __init__(self, packet_sizes: list[int], mu: list[int], delta: list[int]):
        self.packet_sizes = packet_sizes
        self.mu = mu
        self.delta = delta

    def harvest(self) -> list[Combination]:
        combinations = []
        for size in self.packet_sizes:
            g = DataGenerator()
            g.generate_data(size, size)
            packet = g.get_packets()[0]
            for p in self.error_prob:
                for coder in self.coders:
                        if coder == 'SingleParityCheckCode':
                            try:
                                c = harvest_single_combination(coder, packet, 0, 0, p)
                                print(c)
                            except:
                                i = 0
                        else:
                            for m in self.mu:
                                if coder == 'BCHCoder':
                                    for d in self.delta:
                                        try:
                                            c = harvest_single_combination(coder, packet, m, d, p)
                                            print(c)
                                        except:
                                            i = 0
                                else:
                                    try:
                                        c = harvest_single_combination(coder, packet, m, 0, p)
                                        print(c)
                                    except:
                                        i = 0

        return combinations
