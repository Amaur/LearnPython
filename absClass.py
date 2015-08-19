from abc import  ABCMeta, abstractmethod,abstractclassmethod

class Vehicule(metaclass=ABCMeta):

    @abstractmethod
    def change_gear(self):
        pass
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicule):
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color
    def change_gear(self):
        print("Changing gears")
    def start_engine(self):
        print("Starting engine")

class Avion(Vehicule):
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def change_gear(self):
        print(2*"Changing gears")
    def start_engine(self):
        print(2*"Starting engine")

class Date(metaclass=ABCMeta):

    day = 0
    month = 0
    year = 0

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        date1 = cls(day, month, year)
        return date1

date2 =Date.from_string("11-09-2012")
print(type(date2.month))