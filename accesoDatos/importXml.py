import xml.etree.ElementTree as ET
tree = ET.parse('xmlSecundario.xml')
root = tree.getroot()


def sacarNombresCanciones():

    diccionario = {}

    for cancion in root.findall('track'):
        nombre = track.get('name')
        idNombre = track.get('id')

        if cancion not in diccionario:
            diccionario[nombre] = idNombre

    return diccionario
