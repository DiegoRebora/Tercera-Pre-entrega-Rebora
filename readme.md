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
+ Desde el superuser podrá crear, eliminar, modificar y administrar permisos, para los objetos creados para cada modelo

## Instrucciones de navegación y funcionalidad de la APP.
+ Desde la barra de navegación, presente en la página de inicio, se puede acceder a la lista de objetos de cada modelo.
+ Desde dicha lista, podrá a su vez crear un nuevo objeto, o buscar un objeto, por alguno de sus atributos distintivos. 
+ De opta por crear objeto, se abrirá el formulario para la creación de objetos con sus datos.
+ Completado correctamente el formulario, será redirigido al listado de objetos del modelo en cuestión. 
+ De haber errores en el formulario, se mostrará por pantalla en el formulario, que dato debe completarse y como hacerlo correctamente. 

## Versiones
+ Versión 2 creando un nuevo archivo base2.html, desde el que se extienden el resto de los html, como así también un archivo inicio.html
