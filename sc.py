#  ------------------OPCIONAL----------------------------------
# LiBRERIAS PARA PODER GUARDAR NUESTROS DATOS EN UNA BASE DE DATOS EN TIEMPO REAL
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('credentials.json')
default_app = firebase_admin.initialize_app(cred)
db = firestore.client()

def insertDatabase(nameProduct, priceProduct):
    doc_ref = db.collection(u'data').document()
    doc_ref.set({
        u'nameProduct': nameProduct,
        u'priceProduct': priceProduct
    })    

#--------------------------------------------------------------

# -----------------IMPORTANTE-------------------------------
#LIBRERIAS PARA HACER WEB SCRAPING
from bs4 import BeautifulSoup
import requests
#-----------------------------------------------------------


# Contador que nos ayudara a incrementar un valor que sera utilizado para la peticion de mas datos
count = 1

# Ciclo que  ejecutara 7 veces las operaciones dentro de esta
for i in range(0, 7):

    #URL a la cual haremos scraping
    page_link = 'http://www.tiendaamiga.com.bo/categoria-producto/lineablanca/page/'+str(count)+'/'

    #Aquí, obtenemos el contenido de la URL, utilizando la biblioteca de solicitudes.
    page_response = requests.get(page_link, timeout=5)
    
    #Usamos el analizador html para analizar el contenido de la url 
    #y almacenarlo en una variable.
    page_content = BeautifulSoup(page_response.content, 'html.parser')
    
    #Filtramos la informacion de todo el html de acuerdo a la estructura de etiquetas
    #Esto lo almacena como un array de objetos
    filter_tag = page_content.find_all('div', 'box-text box-text-products') 

    #Recorremos cada objeto de nuestro array de objetos y vamos filtrando
    #los diferentes atriibutos
    for select in filter_tag:

        nameProduct = select.a.text 
        priceProduct = select.span.text

        insertDatabase(nameProduct,priceProduct)       
        print(select.span.text)
        print(select.a.text)

    print('Datos guardados de : ',page_link)
    count = count + 1