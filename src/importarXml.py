import xml.etree.ElementTree as ET


def parsearXml(rutaXml):

    # Barricada para comprobar que el xml existe

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

# Assert para comprobar que la longitud del diccionario sea 50

    assert len(diccionario) == 50

# Assert para comprobar que el diccionario no esta vacio

    assert diccionario != {}

    return diccionario
