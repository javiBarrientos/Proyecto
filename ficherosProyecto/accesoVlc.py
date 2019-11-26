import os
import subprocess

# canciones tiene que ser la lista aleatoria
canciones = 'musica'

# comprobar otro path para program files x86
vlcPath = ('C:/Program Files/VideoLAN/VLC/vlc.exe')

subprocess.Popen([vlcPath, canciones])
