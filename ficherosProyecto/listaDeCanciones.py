import random


def listaDeCanciones(diccionario):
    contador = 0
    lista = []
    while contador < len(diccionario):
        for cancion in diccionario:
            cancion = random.choice(list(diccionario.keys()))
            if cancion not in lista:
                lista.append(cancion)
                contador += 1

    return ' '.join(lista)
