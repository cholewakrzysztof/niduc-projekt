import komm
import random
import numpy


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
input_bits = random_bits_array_generator(15)
print("Dane wejściowe:\n", input_bits)

# Kodowanie danych BCH
mu = 3  # Długość słowa kodowego
delta = 7  # Długość danych
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
from SampleClass import SampleClass  # Class import

sampleObj = SampleClass('sample', 15)
sampleObjPlus = SampleClass('samplePlus', 20, 10)

print(sampleObj)
print(sampleObjPlus)

print(sampleObj.sum_object())
print(SampleClass.sum_static(15, 20))
