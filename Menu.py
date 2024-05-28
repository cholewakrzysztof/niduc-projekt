def wyswietl_menu(isExistBC, isExistTC, into):
    width = 30
    print("=" * width)
    if (into == 0):
        print("Główne menu".center(width))
    print("=" * width)
    if (into == 0):
        print("1. Data Generator")
        if (isExistBC == 1):
            print("2. Transmission Controller")
        if (isExistTC == 1):
            print("3. Data Analyzer")
        print("9. Wykonaj test symulacji")
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