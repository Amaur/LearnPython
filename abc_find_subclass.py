from abc import *
from abc_base import *
import abc_register
import abc_subclass

for sc in PluginBase.__subclasses__():
    print(sc.__name__)