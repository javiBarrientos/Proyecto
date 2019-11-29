import random


def listaDeCanciones(diccionario):
    contador = 0
    lista = []

    while contador < len(diccionario):

        for cancion in diccionario:
            cancion = random.choice(list(diccionario.keys()))

            if cancion not in lista:
                comillas = '\"'
                cancionComillas = comillas + cancion + comillas
                lista.append(cancionComillas)
                contador += 1

    listaToString = ' '.join(lista)
    return listaToString
