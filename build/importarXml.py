import xml.etree.ElementTree as ET
import os.path


def parsearXml(rutaXml):
    try:
        os.path(rutaXml)
    except FileNotFoundError:
        print('Este fichero no existe')
    else:
        pass

    tree = ET.parse(rutaXml)
    root = tree.getroot()

    diccionario = {}

    for tracks in root.iter('track'):
        nombreCancion = tracks.find('ruta').text
        idCancion = tracks.get('id')

        diccionario[nombreCancion] = idCancion

    assert diccionario != {}

    return diccionario
