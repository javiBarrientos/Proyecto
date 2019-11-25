from importarXml import parsearXml
from random import random
import logging

assert isinstance(parsearXml, dict)


def lista():
    s = list(range(1, 50))
    random.shuffle(s)
    return s


print(lista())
