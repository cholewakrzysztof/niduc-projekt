class SampleClass:  # Start of class definition
    name = 'Name'
    x = 5
    y = 3

    def __init__(self, name: str, x: int, y: int = 3):  # Constructor
        self.name = name
        self.x = x
        self.y = y  # Optional value in constructor

    def __str__(self):
        return f'Name:{self.name}, X:{self.x}, Y:{self.y}'

    def sum_object(self):  # Object function
        return self.x + self.y

    @staticmethod
    def sum_static(x, y):  # Static function
        return x + y


