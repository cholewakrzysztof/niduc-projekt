from channels.BSCChannel import BSCChannel
from channels.GilbertElliottChannel import GilbertElliottChannel
from coders.BCHCoder import BCHCoder
from coders.HammingCode import HammingCode
from coders.ReedSolomonCoder import ReedSolomonCoder
from coders.SingleParityCheckCode import SingleParityCheckCode


def wyswietl_menu(isExistBC, isPossibleTC, isExistAC, into, opcja):
    width = 30
    print("=" * width)
    if (into == 0):
        print("Główne menu".center(width))
    elif into == 1 and opcja == 200:
        print("Transmission Controller".center(width))
    elif into == 1 and opcja == 300:
        print("Data Analyzer".center(width))
    elif into == 2:
        print("Wybor kodera".center(width))
    print("=" * width)
    if into == 0:
        print("1. Data Generator")
        if isExistBC == True:
            print("2. Transmission Controller")
        if isExistAC == True:
            print("3. Data Analyzer")
        print("9. Wykonaj test symulacji")
    if (into == 1 and opcja == 200):
        print("1. Kanał BSC")
        print("2. Kanał Gilberta-Elliota")
        if isPossibleTC == 1:
            print("3. Wykonaj transmisję")
    if (into == 2 and opcja == 210):
        print("1. Koder BCH")
        print("2. Kod Hamminga")
        print("3. Kod parzystości")
    elif (into == 2 and opcja == 220):
        print("1. Kod Reeda-Solomona")
    if (into > 0):
        print("8. Wróć do poprzedniego menu")
        print("9. Wróć do głównego menu")
    print("0. Wyjscie")
    print("=" * width)

def wybor():
    while True:
        wybor = input("Wybierz opcję: ")
        try:
            wybor = int(wybor)
            return wybor
        except ValueError:
            print("Wybierz opcję: ")

def obliczenie_opcji(into, wybor):
    return wybor*(pow(10,2-into))

def wybor_kanalu(controller, opcja):
    global channel
    if opcja == 210:
        error_probability = input("Wpisz prawodpodobieństwo błędu transmisji: ")
        try:
            error_probability = float(error_probability)
        except ValueError:
            print("Wpisz prawodpodobieństwo błędu transmisji: ")
        channel = BSCChannel(error_probability) # to trzeba przemyśleć XD
    elif opcja == 220:
        p = 0.1  # Prawdopodobieństwo przejścia ze stanu dobrego do złego
        r = 0.2  # Prawdopodobieństwo przejścia ze stanu złego do dobrego
        k = 0.9  # Prawdopodobieństwo poprawnej transmisji w stanie dobrym
        h = 0.1  # Prawdopodobieństwo poprawnej transmisji w stanie złym
        channel = GilbertElliottChannel(p, r, k, h)
    else:
        channel = 0
    controller.set_channel(channel)

def wybor_kodera(controller, opcja, packet_size):
    coder = None
    if opcja == 211:
        mu = 3
        delta = 7
        coder = BCHCoder(mu, delta)
    elif opcja == 212:
        mu = 3
        coder = HammingCode(mu)
    elif opcja == 213:
        n = packet_size + 1
        coder = SingleParityCheckCode(n)
    elif opcja == 221:
        n = packet_size + 3
        k = packet_size
        coder = ReedSolomonCoder(n, k)
    if coder is not None:
        controller.set_coder(coder)
    else:
        raise ValueError("Nieprawidłowa opcja kodera: {}".format(opcja))

def nazwa_kodera(opcja):
    coders = {211: "bch", 212: "hamming", 213: "parzystosc", 221: "reedsolomon"}
    return coders.get(opcja)