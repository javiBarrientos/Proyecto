import xml.etree.ElementTree as ET


def parsearXml(rutaXml):
    tree = ET.parse(rutaXml)
    root = tree.getroot()

    diccionario = {}

    for tracks in root.iter('track'):
        nombreCancion = tracks.find('ruta').text
        idCancion = tracks.get('id')

        diccionario[nombreCancion] = idCancion

    assert diccionario != {}

    return diccionario
