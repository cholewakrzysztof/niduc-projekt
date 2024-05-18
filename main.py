import random

import komm
import numpy

import TransmissionController
from DataAnalyzer import DataAnalyzer
from common.RawBitChain import RawBitChain


# Dane wejściowe
def random_bits_array_generator(length):
    arr = [random.randint(0, 1) for i in range(0, length)]
    return numpy.array(arr)

# Kodowanie danych BCH
def bch_encode(input_bits, mu, delta):
    bch = komm.BCHCode(mu, delta)
    encoder = komm.BlockEncoder(bch)
    encoded_data = encoder(input_bits)
    return encoded_data

# Symulacja przesyłu przez BSC
def bsc_simulation(encoded_data, error_probability):
    channel = komm.BinarySymmetricChannel(error_probability)
    return channel(encoded_data)

# Dekodowanie danych
def decoder(output_bits, mu, delta,):
    bch = komm.BCHCode(mu, delta)
    decoder = komm.BlockDecoder(bch)
    decoder_data = decoder(output_bits)
    return decoder_data


# Dane wejściowe
input_bits = random_bits_array_generator(32)
print("Dane wejściowe:\n", input_bits)

# Kodowanie danych BCH
mu = 5 # Długość słowa kodowego
delta = 31  # Długość danych
encoded_data = bch_encode(input_bits, mu, delta)
print("Dane zakodowane BCHe:\n", encoded_data)

# Symulacja przesyłu przez BSC
error_probability = 0.1  # Prawdopodobieństwo błędu
output_bits = bsc_simulation(encoded_data, error_probability)
print("Dane wyjściowe po przesyłaniu przez BSC:\n", output_bits)

# Dekodowanie danych
decoder_data = decoder(output_bits, mu, delta)
print("Dane wyjściowe po dekodowaniu:\n", decoder_data)

print('Sample object code execution')

data_analyzer = DataAnalyzer()

controller = TransmissionController.TransmissionController(mu, delta, error_probability)
chain = RawBitChain(random_bits_array_generator(200))
controller.receive_data(chain)
controller.start_transmission()
print(controller.get_input())
print(controller.get_output())

data_analyzer.add_test_data(controller.length, controller.InBits, controller.OutBits)

data_analyzer.save_report('C:\\Users\\Admin\\Desktop\\NIDUC\\results.csv')



