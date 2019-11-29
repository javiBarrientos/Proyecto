import os


def accederVlc(rutaVlc, lista):
    return os.popen(rutaVlc + " " + lista)
