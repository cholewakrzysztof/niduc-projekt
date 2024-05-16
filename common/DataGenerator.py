import os
import random
from common.RawBitChain import RawBitChain


class DataGenerator:
    def __init__(self):
        self.bit_chain = ""
        self.packets = []

    def reader(self, file_path):
        if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
            choice = input("Plik nie istnieje. Czy chcesz wygenerować (L)osową tablicę czy wprowadzić (W)łasne dane? ").strip().upper()
            if choice == 'L':
                length = int(input("Wprowadź długość ciągu danych: "))
                data = self.generate_random_data(length)
            elif choice == 'W':
                data = input("Wprowadź dane: ")
            else:
                raise ValueError("Nieprawidłowa opcja")
        else:
            with open(file_path, 'r') as file:
                data = file.read().strip()

        if all(char in '01' for char in data):
            choice = input("Wykryto tylko znaki '0' i '1'. Czy chcesz, żeby tworzyły one tablicę (C)harów czy tablicę "
                           "(B)itów? ").strip().upper()
            if choice == 'C':
                char_array = list(data)
                self.bit_chain = ''.join([bin(ord(char))[2:].zfill(8) for char in char_array])
            elif choice == 'B':
                self.bit_chain = data
            else:
                raise ValueError("Nieprawidłowa opcja")
        else:
            char_array = list(data)
            self.bit_chain = ''.join([bin(ord(char))[2:].zfill(8) for char in char_array])

    def generate_random_data(self, length):
        return ''.join(random.choice('01') for _ in range(length))

    def split_into_packets(self, packet_size):
        if packet_size <= 0:
            raise ValueError("Rozmiar pakietu musi być większy od zera")

        remainder = len(self.bit_chain) % packet_size
        padding = packet_size - remainder if remainder != 0 else 0
        if padding > 0:
            print("Uwaga: Dopełniono ostatni pakiet zerami.")

        padded_bit_chain = self.bit_chain + '0' * padding
        self.packets = [RawBitChain(padded_bit_chain[i:i + packet_size]) for i in
                        range(0, len(padded_bit_chain), packet_size)]

    def display_packets(self):
        print("Pakiety:")
        for i, packet in enumerate(self.packets):
            print(f"Packet {i + 1}: {packet.chain}")

    def data_generator(self):
        file_path = input("Jeśli chcesz wprowadzić dane z pliku, wprowadź nazwę pliku, w przeciwnym razie zostaw puste: ")
        self.reader(file_path)

        packet_size = int(input("Wprowadź rozmiar pakietu: "))
        self.split_into_packets(packet_size)
        self.display_packets()

if __name__ == "__main__":
    generator = DataGenerator()
    generator.data_generator()