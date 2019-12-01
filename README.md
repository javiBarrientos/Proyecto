# Proyecto VLC

Esta practica es un proyecto transversal del curso de Programación Web Dual del instituto Francesc de Borja Moll.

## De que trata el proyecto

Construir un programa que genere una lista de reproducción aleatoria (50 canciones como mínimo) de las canciones que tienes en tu biblioteca de canciones de tu máquina. El script llama a VLC una vez que la lista esta creada y la música empieza a sonar en tu pc.

## Que hemos hecho

En este proyecto hemos usado la metodologia en casacada, decidimos utiliar esta metodologia porque nos parecia la mas idonea ya que fuimos haciendo modulo por modulo comprobando que la salida que obteniamos era la esperada y como ultimo los juntamos todos en uno.

Tambien en este proyecto decidimos implementar todo lo aprendido hasta ahora de la programacion por modulos, creando 4 ficheros. 
- El main que es el directorio que contiene todos los imports de los demas modulos y donde definimos las variables de la ruta de xml y vlc. 
- El fichero de importarXml donde parseamos el xml y creamos un diccionario con la ruta de la cancion y la id.
- El fichero listaDeCanciones donde usamos el diccionario para coger llaves y generar una lista aleatoria con las rutas de esas canciones, y donde convertimos esa lista en un string para enviarlo al VLC.
- Y como ultimo fichero accesoVlc en este fichero usamos el resultado del modulo de listaDeCanciones que es un string con la ruta y la variable de la ruta del vlc para mandarlo por consola de windows y que se ejecute.

Los participantes de este proyecto són:

- Samuel Ferragut Molina
- Javier Barrientos Fernandez