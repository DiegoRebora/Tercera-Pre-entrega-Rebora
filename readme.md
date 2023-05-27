# ProyectoCoder

## Instrucciones instalar proyecto en local
+ Crea una carpeta contenedora madre
+ Abre la consola y ubicate en la carpeta madre
+ Crea y activa el ambiente virtual
+ Clona este proyecto en la carpeta madre
+ Entra en la carpeta que acabas de clonar
+ Para instalar las dependencias corre este comando:

```
pip install -r requirements.txt
```

## Instrucciones para entrar al panel aministrativo de Django
+ En consola, crear un superuser:
```
python manage.py createsuperuser
```
+ Acceder con user y password via:
```
127.0.0.1:8000/admin
```
+ Desde el superuser podrá crear, eliminar, modificar y administrar todos los objetos creados para cada modelo, como así también sus permisos.

## Instrucciones de navegación y funcionalidad de la APP.
+ Desde la barra de navegación, presente en la página de inicio, se puede acceder a la lista de objetos de cada modelo, como así también, optar por registrarse o iniciar sesión.
+ La lista de objetos de cada modelo, es accesible por todo usuario del sitio.
+ Desde la lista de objetos de cada modelo, todo usuario puede a su vez, conocer el detalle de cada objeto, como así también buscar un objeto por algúno de sus atributos distintivos.
+ Desde dicha lista, podrá a su vez crear un nuevo objeto, según se trate de un usuario no registrado, usuario registrado o super usuario.
+ Los objetos de los modelos "Jugadores", "Marca", "Circuito", se encuentran limitados para su creación, edición o eliminación, únicamente, por el superusuario. 
+ Los objetos del modelo "Comentario", se encuentran habilitados para su creación, solo por parte de usuarios registrados. La edición o eliminación de los objetos "comentario", se encuentran limitadas al usuario que hubiera creado el objeto.
+ Los objetos del modelo "Comentario", tendrán dos filtros de búsqueda independientes, ya fuere por título o por contenido del texto. 
+ Para la creación de objetos, se dirigirá al formulario para la creación de objetos con sus datos.
+ Completado correctamente el formulario, será redirigido al listado de objetos del modelo en cuestión. 
+ De haber errores en el formulario, se mostrará por pantalla en el formulario, que dato debe completarse y como hacerlo correctamente. 
+ Para el inicio de sesión se solicitará nombre de usuario y contraseña.
+ Los usuarios logueados tendrán acceso a todas aquellas funcionalidades disponibles para usuarios no logueados, más la posibilidad de crear, editar o eliminar sus propios comentarios. 
+ A su vez, podrán completar datos de su perfil, como nombre, apellido y dirección de e-mail. 
+ Una vez logueado correctamente, contará con un menú desplegable en la barra de navegación, desde el que podrá editar tan su perfil, como su avatar. 
+ En la edición de su perfil, podrá modifiicar, nombre, apellido, e-mail y contraseña.
+ Podrá modifica a su vez modifiicar el avatar elegido. 
