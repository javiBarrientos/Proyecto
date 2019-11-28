import xml.etree.ElementTree as ET


def parsearXml(rutaXml):
    tree = ET.parse(rutaXml)
    root = tree.getroot()

    diccionario = {}

    for tracks in root:
        for track in tracks.findall('track'):
            nombreCancion = track.find('ruta').text
            idCancion = track.get('id')

            diccionario[nombreCancion] = idCancion

            diccionario = {key.strip(): value for key,
                           value in diccionario.items()}

    assert isinstance(diccionario, dict)

    return diccionario
