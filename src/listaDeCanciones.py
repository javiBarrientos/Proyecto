import random

# En esta parte del codigo vamos a generar una lista de canciones aleatoria y despues lo pasaremos a string utilizando un join


def listaDeCanciones(diccionario):

    assert isinstance(diccionario, dict)

    contador = 0
    lista = []

    while contador < len(diccionario):

        cancion = random.choice(list(diccionario.keys()))
        comillas = '\"'
        cancionComillas = comillas + cancion + comillas

        if cancionComillas not in lista:
            lista.append(cancionComillas)
            contador += 1

    assert lista != []

    assert len(lista) == len(diccionario)

    listaToString = ' '.join(lista)

    assert lista != ""

    return listaToString
