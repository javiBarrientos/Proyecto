from importarXml import parsearXml
from listaDeCanciones import listaDeCanciones


def main():
    rutaXml = 'libreriasXml/musicaProyecto.xml'
    data = parsearXml(rutaXml)
    cancionesAleatorias = listaDeCanciones(data)
    print(cancionesAleatorias)


main()
