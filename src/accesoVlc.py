import os

# Este try except comprueba que la ruta que tenemos de vlc existe, antes de operar con el


def accederVlc(rutaVlc, lista):
    try:
        exec(rutaVlc)
    except OSError:
        print('El sistema no puede encontrar la ruta especificada')
    else:
        pass

    assert isinstance(rutaVlc, str)
    assert isinstance(lista, str)

    return os.popen(rutaVlc + " " + lista)
