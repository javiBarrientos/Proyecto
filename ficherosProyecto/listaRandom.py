from importXml import parsearXml
from random import random

assert isinstance(parsearXml, dict)

playlist = []


def listaRandom():
    i = 0
    while i < 50:
        cancion = random.choice(parsearXml.keys())
        if cancion not in playlist:
            playlist.append(cancion)
            i = i+1
    return playlist


print(listaRandom())
