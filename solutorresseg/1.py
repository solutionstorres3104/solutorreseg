import os
import requests
import json

url1 = 'http://api.mercadopublico.cl/servicios/v1/publico/licitaciones.json?codigo='
url2 = '2423-38-LR22'
url3 = '&ticket=F8537A18-6766-4DEF-9E59-426B4FEE2844'
url = url1+url2+url3
response = requests.get(url)
if response.status_code ==200:
        content = response.content
       

        droplets = response.json()
        
        
        
        droplet_list = []
        xx = range(len(droplets))
        for i in range(len(droplets['Listado'])):
                droplet_list.append(droplets['Listado'][i])
        print(droplet_list)
       
        

        ###users = listado[0][1]
        ###address = lista['MontoEstimado']
        
        ###resp = response.json()
 
        ###print(resp[1])
        

        
       ### users = listado[0]
       ### print(users)
       ### address = users['CodigoOrganismo']
       ### print(address)

        