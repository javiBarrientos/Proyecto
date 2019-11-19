import xml.etree.ElementTree as ET
tree = ET.parse('C:/Users/Javi/Desktop/proyecto/accesoDatos/xmlSecundario.xml')
root = tree.getroot()

# barricada para comprobar que entra


def nombresCanciones():

    listaNombreCanciones = []

    for tracks in root:  # child in root
        for track in tracks:  # subchild in child
            for name in track.findall('name'):  # name in subchild
                nombre = track.get('name')

                if nombre not in listaNombreCanciones:
                    listaNombreCanciones.append(nombre)

# barricada para comprobar que sale

    return listaNombreCanciones
