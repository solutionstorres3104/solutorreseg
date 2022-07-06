
import os
import requests
import json


def get_licita(licita):
    
    url1 = 'http://api.mercadopublico.cl/servicios/v1/publico/licitaciones.json?codigo='
    url2 = licita
    url3 = '&ticket=F8537A18-6766-4DEF-9E59-426B4FEE2844'
    url = url1+url2+url3
    
    
    response = requests.get(url)
    if response.status_code ==200:
        content = response.content
        #file = open('licitaciones.html','wb')
        #file.write(content)
        
        
        
        licitas = response.json()
        listado = licitas['Listado']
        users = listado[0]
        address = users['MontoEstimado']
        print(users)

        content = response.content
        jsondecoded = json.loads(content)
       

        for entity in jsondecoded["Listado"]:
          entityFechas = entity["Fechas"]

       
        xFechaPublicaciont = str(entityFechas['FechaPublicacion']) 
        print(xFechaPublicaciont)
 
       
        return users