from ..accesoDatos.importXml import nombresCanciones
from random import random

assert isinstance(listaNombreCanciones, dict)

playlist = []


def listaRandom():
    i = 0
    while i < 50:
        cancion = random.choice(listaNombreCanciones.keys())
        if cancion not in playlist:
            playlist.append(cancion)
            i = i+1
    return playlist
