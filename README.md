# Proyecto VLC

Esta practica es un proyecto transversal del curso de Programación Web Dual del instituto Francesc de Borja Moll.

## De que trata el proyecto

Construir un programa que genere una lista de reproducción aleatoria (50 canciones como mínimo) de las canciones que tienes en tu biblioteca de canciones de tu máquina. El script llama a VLC una vez que la lista esta creada y la música empieza a sonar en tu pc.

## Proceso

En este proyecto hemos usado la metodologia en casacada, decidimos utiliar esta metodologia porque nos parecia la mas idonea ya que fuimos haciendo modulo por modulo comprobando que la salida que obteniamos era la esperada y como ultimo los juntamos todos en uno.

Tambien en este proyecto decidimos implementar todo lo aprendido hasta ahora de la programacion por modulos, creando 4 ficheros. 
- El main que es el directorio que contiene todos los imports de los demas modulos y donde definimos las variables de la ruta de xml y vlc. 
- El fichero de importarXml donde parseamos el xml y creamos un diccionario con la ruta de la cancion y la id.
- El fichero listaDeCanciones donde usamos el diccionario para coger llaves y generar una lista aleatoria con las rutas de esas canciones, y donde convertimos esa lista en un string para enviarlo al VLC.
- Y como ultimo fichero accesoVlc en este fichero usamos el resultado del modulo de listaDeCanciones que es un string con la ruta y la variable de la ruta del vlc para mandarlo por consola de windows y que se ejecute.

Nuestro trabajo esta enfocado en usar la metodologia en cascada, elegimos esta metodologia porque fue la que mas se adaptaba a nuestra forma de trabajar, tambien decidimos implementar todo lo aprendido hasta hoy sobre la programacion modulada.
En nuestra programacion modulada tenemos el proyecto dividido en 4 modulos, cada uno de ellos lo importamos a un modulo llamado main donde.
El fichero main contiene todos los imports de los demas modulos, eso quiere decir que todos los modulos estan conectados entre si por el modulo main, aqui tambien tenemos indicadas las variables de las rutas del xml y donde esta instalado vlc, de esta forma si el usuario quiere cambiar dependiendo de donde tenga el xml o el fichero xml solo tendra que buscar en el fichero principal.

El fichero importarXml esta definido dentro de main como data, esto lo usaremos mas adelante para el modulo de canciones aleatorias. Dentro del modulo de importarXml hemos importado la libreria de xml.etree para poder usar todas sus funciones, antes de parsear el xml en memoria tenemos una barricada que comprueba que ese fichero exista, en el caso de que no exista cortarea el programa y te imprimira un mensaje por terminal. Si el fichero esta bien y no hay ningun problema el fichero xml se parseara a memoria, cogiendo el contenido de la variable rutaXml del fichero main, inicializamos un diccionario vacio, recorremos el primer elemento del fichero xml buscando dentro de tracks y en todo sus hijos el elemento 'track', seguido en la variable de nombreCancion le añadimos como texto lo que esta dentro de la etiqueta 'ruta' dentro del padre track, y como segunda varible que guarde el id o atributo del elemento track, como ultimo añadimos al diccionario cada uno de esos elementos nombreCancion como key e idCancion como value, antes de devolver el resultado del diccionario hemos creado un assert que comprube que el diccionario no esta vacio.

El fichero listaDeCanciones tiene como import la funciona random ya que lo usaremos para coger un elemento aleatorio de la variable diccionario, esta variable esta definida en el fichero main con el nombre de data, antes de nada hemos creado un assert que compruebe que el diccionario que nosotros le pasamos es un diccionario, ahora si una vez comprobado eso inicializamos un contador y una lista vacia, abrimos con un while que mientra el contador sea menor que la longitud del diccionario siga incrementando, iniciamos tres variables, la variable de cancion que nos pasa las keys del diccionario a una lista y elige aleatoriamente una cancion, la variable de comillas que la usaremos para añadir comillas dobles a nuestro string, y como ultimo sera la cancion concatenado con la variable de comillas dobles de esta forma los espacios que tienen las canciones no seran un problema para vlc. Las siguientes lineas son dos asserts que comprueban que la lista no esta vacia, que la lista tenga la misma longitud que el diccionario, despues iniciamos un string que lo usaremos para convertir esa lista en una string y un ultimo assert que compruebe que el string no esta vacio.

En el ultimo modulo es en el que accedemos a vlc como no es un modulo que recibe informacion nuestra tendremos que hacer una barricada para comprobar que la ruta que tenemos en la variable rutaVlc definida en el fichero main como rutaVlc no este mal escrita o vlc no se encuentr ahi, el try funciona intentando ejecutar la rutaVlc el except es OSerror un error del sistema que nos indica que esa ruta no esta existe mostrando por pantalla el mensaje que querramos, despues de eso queremos comprobar que la informacion que nosotros le mandamos es correcta y creamos dos assert que comprueben que esas dos variables sean string y le mandamos por consola de comandos la ruta del vlc y el string con canciones random concatenado por un espacio en blanco. El modulo que importamos que es os nos sirve para usar popen.


Los participantes de este proyecto són:

- Samuel Ferragut Molina
- Javier Barrientos Fernandez