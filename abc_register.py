import abc
from abc import *
from abc_base import PluginBase

class RegisteredImplementation():
    def load(self,input):
        return input.read()
    def save(self, output,data):
        return  output.write(data)

PluginBase.register(RegisteredImplementation)

if __name__=="__main__":
    print('Subclass: ',issubclass(RegisteredImplementation,PluginBase))
    print('Isintance: ',isinstance(RegisteredImplementation(),PluginBase))