import os
import subprocess
from proyectoVLC import rutaVLC, rutaListaMusica

# canciones tiene que ser la lista aleatoria
canciones = rutaListaMusica()

# comprobar otro path para program files x86
vlc = rutaVLC()

subprocess.Popen([vlc, canciones])
