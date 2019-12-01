import xml.etree.ElementTree as ET

# Antes de empezar a parsear el xml hacemos un try except para comprobar que ese xml existe


def parsearXml(rutaXml):
    try:
        open(rutaXml)
    except FileNotFoundError:
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
