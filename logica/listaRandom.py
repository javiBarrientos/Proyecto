from random import random
from ../accesoDatos/diccionario import x


playlist = []


def listaRandom(canciones):
    i = 0
    while i < 50:
        cancion = random.choice(libreria.keys())
        if cancion not in playlist:
            playlist.append(cancion)
            i = i+1
    return playlist
