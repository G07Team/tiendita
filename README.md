# PROYECTO TIENDITA ONLINE 🛒

_Acá va un párrafo que describe lo que es el proyecto_

## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._


### Pre-requisitos 📋


- Git: https://git-scm.com/downloads

- Python 3.6 o superior -> https://www.python.org/downloads

- Tener instalado la librería de python 'virtualenv'. Si no la tienes puedes instalarla con el siguiente comando:
```
pip install virtualenv
```

### Instalación 🔧

_1. Abrir la carpeta en donde almacenarás el proyecto e ingresar al 'Terminal' en esa ubicación_

_2. En el terminal ejecutar el siguiente comando para descargar el repositorio_
```
git clone https://github.com/navichicken/tiendita
```
_3. Ejecutar el siguiente comando para ingresar a la carpeta_
```
cd tiendita
```
_4. Crear un entorno virtual con el siguiente comando_
```
virtualenv venv
```
_5. Activar el entorno virtual con el siguiente comando. Una vez activado podrás visualizar (venv) al inicio de la ruta en el terminal._
```
venv\Scripts\activate
```
_6. Ejecutar el siguiente comando para instalar todas las dependencias_
```
pip install -r requirements.txt
```
_7. Luego de haber instalado las dependencias, ejecutar el siguiente comando para correr las migraciones._
```
python manage.py migrate
```
_8. Ejecutar el siguiente comando para crear el superusuario. Ingresar el usuario, correo y password cuando te lo pida._
```
python manage.py createsuperuser
```
_9. Listo ya configuraste lo necesario. Ahora ejecuta el siguiente comando para levantar la aplicación._
```
python manage.py runserver
```
Ahora en tu navegador dirigite a http://127.0.0.1:8000/


## Posibles errores que ocurran durante la instalación y configuración 🤬🤬
[Agregar el troubleshooting luego]

Si estás una versión reciente de Mysql, puede que ocurra un error en el paso de las migraciones, para solucionarlo puedes ejecutar el siguiente comando SQL, desde tu usario root.
```
CREATE USER 'sigepe_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'sigepe_pass';
GRANT ALL PRIVILEGES ON sigepe_db.* TO 'sigepe_user'@'localhost';
```
Donde _DB_USERNAME=sigepe_user_, _DB_PASSWORD=sigepe_pass_ y _DB_DATABASE=_sigepe_db_

## Proyecto forked from https://github.com/divanov11/django_ecommerce_mod5

## Construido con 🛠️

_Menciona las herramientas que utilizaste para crear el proyecto_

* [Django](https://docs.djangoproject.com/en/3.1/) - El framework web usado
* [Python](https://docs.python.org/3/) - Lenguaje de programación
