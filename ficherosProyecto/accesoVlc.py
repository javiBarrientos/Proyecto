import subprocess
import shlex


def accederVlc(ruta, lista):
    abrirVlc = shlex.split(ruta, lista)
    subprocess.Popen(abrirVlc)
