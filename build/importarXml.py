import xml.etree.ElementTree as ET


def parsearXml(rutaXml):
    try:
        open(rutaXml)
    except OSError:
        print('Este fichero ' + rutaXml + ' no existe')
        exit()
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
