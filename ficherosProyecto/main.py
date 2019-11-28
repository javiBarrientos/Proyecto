from importarXml import parsearXml
from listaDeCanciones import listaDeCanciones


def main():
    rutaXml = 'libreriasXml/musicaProyecto.xml'
    data = parsearXml(rutaVlc)
    cancionesAleatorias = listaDeCanciones(data)
    print(cancionesAleatorias)


main()
