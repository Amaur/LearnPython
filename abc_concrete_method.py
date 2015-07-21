#from abc import *
import abc


class ABCWithConcreteImplementation(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def retrieve_values(self,input):
        print('basee class readind data')
        return input.read()

    class ConcreteOverride(ABCWithConcreteImplementation):
        def retrieve_values(self,input):
            base_data = super(ConcreteOverride,self).retrieve_values(input)