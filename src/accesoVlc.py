import os


def accederVlc(rutaVlc, cancionesAleatorias):

    # He creado esta barricada para comprobar que la ruta del vlc es correcta

    try:
        exec(rutaVlc)
    except OSError:
        print('El sistema no puede encontrar la ruta especificada')
    else:
        pass

# Tambien he creado estos assert para comprobar que las dos rutas son string

    assert isinstance(rutaVlc, str)
    assert isinstance(cancionesAleatorias, str)

    return os.popen(rutaVlc + " " + cancionesAleatorias)
