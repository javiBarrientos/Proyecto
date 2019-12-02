from importarXml import parsearXml
from listaDeCanciones import cancionesRandom
from accesoVlc import accederVlc


def main():
    rutaXml = 'C:\\Users\\Javi\\Desktop\\proyecto\\lib\\musicaProyecto.xml'
    rutaVlc = '"C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"'
    diccionario = parsearXml(rutaXml)
    cancionesAleatorias = cancionesRandom(diccionario)
    accederVlc(rutaVlc, cancionesAleatorias)


if __name__ == "__main__":
    main()
