import xml.etree.ElementTree as ET


def parsearXml(rutaXml):
    tree = ET.parse(rutaXml)
    root = tree.getroot()

    diccionario = {}

    for tracks in root.findall('ruta'):
        nombreCancion = tracks.findtext
        for track in tracks.findall('track'):
            idCancion = track.get('id')

            diccionario[nombreCancion] = idCancion

    assert isinstance(diccionario, dict)

    return diccionario
