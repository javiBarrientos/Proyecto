from importarXml import parsearXml
from listaDeCanciones import listaDeCanciones
from accesoVlc import accederVlc


def main():
    rutaXml = 'libreriasXml/musicaProyecto.xml'
    rutaVlc = 'C:/Program Files/VideoLAN/VLC/vlc.exe'
    data = parsearXml(rutaXml)
    cancionesAleatorias = listaDeCanciones(data)
    accesoVlc = accederVlc(rutaVlc, cancionesAleatorias)


main()
