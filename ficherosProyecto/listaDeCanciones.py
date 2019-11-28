import random


def listaDeCanciones(diccionario):
    i = 0
    lista = []
    comilla = '\"'
    while i < len(diccionario):
        for cancion in diccionario:
            cancion = random.choice(list(diccionario.keys()))
            if cancion not in lista:
                lista.append(cancion)
                i += 1
    return ' '.join(lista)
