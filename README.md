# Web Scraping
Este proyecto es un ejemplo de web Scraping que rescata la información de una pagina web y la almacena en una base de datos en Firebase (Firestone) .
Y luego tenemos un archivo index.html que forma parte del ejemplo que su función es de obtener la información almacenada en la base de datos de Firebase en tiempo real 

### Pasos que sigue el Algoritmo :
- Hacer una petición Http a una URL con librería **requests**
- Almacenar la información en una variable
- Transformar la información en un objeto para manipular fácilmente el código HTML que tuvimos como respuesta con librería **beautifulsoup4**
- Filtrar la información de acuerdo a la estructura HTML que ya debemos saber para obtener solo las etiquetas donde están los datos que nos interesa.
- Almacenar esa información (en este caso la almaceno en una base de datos **firebase** para luego obtener esta información mediante el archivo index.html en tiempo real y visualizarla.
### Instalación del proyecto :
Este proyecto lo levante con [Python](https://python.org/) v3+ especialmente con la versión 3.7.1 .

Nos dirigimos al directorio clonado 
```sh
$ cd webScraping
```
Instalamos todas las dependencias
```sh
$ pip install -r requirements.txt
```
Levantamos nuestro index.html con un servidor local (en mi caso levante con **serve** de nodejs ) o directamente en nuestro navegador abrimos el archivo index.html
```sh
$ serve index.html
```

Levantamos nuestro proyecto
```sh
$ python sc.py
```