import xml.etree.ElementTree as ET


def parsearXml(rutaXml):
    tree = ET.parse(rutaXml)
    root = tree.getroot()

    try:
        f = open(rutaXml)
    except FileNotFoundError:
        print('Este fichero no existe')
    else:
        pass

    diccionario = {}

    for tracks in root.iter('track'):
        nombreCancion = tracks.find('ruta').text
        idCancion = tracks.get('id')

        diccionario[nombreCancion] = idCancion

    assert diccionario != {}

    return diccionario
