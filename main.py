import requests
import json

# Variables
url="https://apitransporte.buenosaires.gob.ar/colectivos/vehiclePositions"
aut = {
    'json':1,
    'agency_id':71,
    '_id"': 30196,
    'client_id':"b05ee44f5ddd414dad71815064295290",
    'client_secret':"c28337fb1C964e6FAe37b2AC0028d222" 
}

# Funciones
def imprimeOrdenado(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)



response = requests.get(url,aut)
print(response.status_code)

arreglo71 = response.json()['_entity'] # creo una lista de diccionarios

for i in range(len(arreglo71)):
    
    print(arreglo71[i].get('_vehicle').get('_position').get('_longitude'))

