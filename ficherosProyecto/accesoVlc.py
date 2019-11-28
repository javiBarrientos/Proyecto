import subprocess


def accederVlc(ruta, lista):
    subprocess.Popen([ruta, lista])
