import os


def accederVlc(rutaVlc, lista):
    try:
        f = exec(rutaVlc)
    except OSError:
        print('El sistema no puede encontrar la ruta especificada')
    else:
        pass

    return os.popen(rutaVlc + " " + lista)
