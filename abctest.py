from abc import *


class Vehicule():
    __metaclass__ = ABCMeta
    @abstractmethod
    def quoiq(self):
        raise NotImplemented

    @abstractmethod
    def andnow(self):
        raise NotImplemented

class Car(Vehicule):
    def __init__(self,model,year):
        self.model =model
        self.year = year
    def quoiq(self):
        print (self.model)
car= Car("Toyato",2003)
car.quoiq()