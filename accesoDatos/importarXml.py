import xml.etree.ElementTree as ET


def parsearXml():
    tree = ET.parse(
        'C:/Users/Javi/Desktop/proyecto/accesoDatos/xmlSecundario.xml')
    root = tree.getroot()

    diccionario = {}

    for tracks in root:
        for track in tracks:
            nombreCancion = track.find('name').text
            idCancion = track.get('id')

            diccionario[nombreCancion] = idCancion

            diccionario = {x.translate(
                {32: None}).strip(): y for x, y in diccionario.items()}

    assert isinstance(diccionario, dict)
    return diccionario


print(parsearXml())
