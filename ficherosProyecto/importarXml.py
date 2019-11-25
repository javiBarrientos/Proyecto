import xml.etree.ElementTree as ET


def parsearXml():
    tree = ET.parse('xmlSecundario.xml')
    root = tree.getroot()

    diccionario = {}

    for tracks in root:
        for track in tracks:
            nombreCancion = track.find('name').text
            idCancion = track.get('id')

            diccionario[nombreCancion] = idCancion

            diccionario = {key.strip(): value for key,
                           value in diccionario.items()}

    assert isinstance(diccionario, dict)

    return diccionario
