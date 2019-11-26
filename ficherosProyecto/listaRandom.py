from importarXml import parsearXml
import random


def lista():
    s = list(range(1, 50))
    random.shuffle(s)
    return s


print(lista())
