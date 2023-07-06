import requests
import json

#Se importa lo necesario de la galeria de python para tratar con json y urls

#Establecemos nuestra url como variable
url= "https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-3/api-proyecto/main/products.json"

#Utilizamos el requests.get() para obtener el contenido de dicha url en una nueva variable
response = requests.get(url)

#y para terminar el tratado de estos datos, los convertimos en json para facilitar proximos procesos
data = response.json()
