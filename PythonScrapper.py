
import requests
print('Consultando la web...')
page = requests.get("https://www.pccomponentes.com/thrustmaster-hotas-warthog")
#page = requests.get("https://www.pccomponentes.com/thrustmaster-f-a-18c-hornet-hotas-add-on-grip")

from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')

#NO BORRAR - SIRVE PARA VER EN DETALLE EL CONTENIDO DE LA WEB
#print(soup.prettify())
print('Extrayendo los datos...')
result = soup.find("div", {"class":"precioMain h1"})
precioActual_texto = result.text
#Limpiamos el resultado de simbolos, de saltos de carro y convertimos la coma en punto
precioActual_texto_Limpio1 = precioActual_texto.replace('€', '')
precioActual_texto_Limpio2 = precioActual_texto_Limpio1.replace('\n','')
precioActual_texto_Limpio3 = precioActual_texto_Limpio2.replace(',','.')
print(precioActual_texto_Limpio2)
precioActual = float(precioActual_texto_Limpio3)#necesario cambiar la coma por punto para la conversion a float
print('Analizando los datos...')
#Establecemos el precio deseado - pdte mejorarlo para pedirlo por pantalla, etc de momento a pinrel
#precioDeseado = int(input("Introduce el precio máximo deseado:"))
precioDeseado = 400
print ("\nEl precio máximo deseado para este producto es de "+ str(precioDeseado)+"€\n")

global hayOferta
#Calcula el precio
import Funciones_Scrapper
hayOferta = Funciones_Scrapper.Oferta_Precio_Deseado(precioActual,precioDeseado)

if(hayOferta):
    print("Tenemos OFERTA! - Avisamos al usuario!")
    #avisar por telegram
    import Aviso_Telegram
    Aviso_Telegram
else:
    print("No hay oferta.")
