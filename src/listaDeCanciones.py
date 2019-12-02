import random


def cancionesRandom(diccionario):

    # Assert para comprobar que el diccionario es un diccionario

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

# Aqui he creado dos assert:
# Uno que comprueba que la lista no esta vacia
# Y este compurba que la longituda de la lista es igual a la del diccionario

    assert lista != []

    assert len(lista) == len(diccionario)

    listaToString = ' '.join(lista)

# Como ultimo assert que el string no este vacio

    assert lista != ""

    return listaToString
