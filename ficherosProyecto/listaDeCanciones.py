from importarXml import parsearXml
import random


def listaDeCanciones():
    diccionario = parsearXml()
    i = 0
    lista = []
    while i < len(diccionario):
        for cancion in diccionario:
            cancion = random.choice(list(diccionario.keys()))
            if cancion not in lista:
                lista.append(cancion)
                i += 1
    return lista


print(listaDeCanciones())
