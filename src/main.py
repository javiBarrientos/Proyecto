from importarXml import parsearXml
from listaDeCanciones import listaDeCanciones
from accesoVlc import accederVlc


def main():
    rutaXml = 'C:\\Users\\Javi\\Desktop\\proyecto\\lib\\musicaProyecto.xml'
    rutaVlc = '"C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"'
    data = parsearXml(rutaXml)
    cancionesAleatorias = listaDeCanciones(data)
    accederVlc(rutaVlc, cancionesAleatorias)


if __name__ == "__main__":
    main()
