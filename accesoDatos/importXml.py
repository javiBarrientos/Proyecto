import xml.etree.ElementTree as ET
tree = ET.parse('C:/Users/Javi/Desktop/proyecto/accesoDatos/xmlSecundario.xml')
root = tree.getroot()


for tracks in root:
    for track in tracks:
        print(track[0].text)
