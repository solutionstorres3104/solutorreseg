import os
import requests
import json

url1 = 'http://api.mercadopublico.cl/servicios/v1/publico/licitaciones.json?codigo='
url2 = '2179-30-LP22'

url3 = '&ticket=F8537A18-6766-4DEF-9E59-426B4FEE2844'
url = url1+url2+url3
    
    
response = requests.get(url)
if response.status_code ==200:
    licitas = response.json()
    listado = licitas['Listado']
    users = listado[0]
    address = users['MontoEstimado']
    codigo_externo=(users["CodigoExterno"])
    nom= (users["Nombre"])
    des= (users["Descripcion"])
    monto = (users["MontoEstimado"])
    fecha =(users["FechaCierre"])
    comp_rut = users['Comprador']['RutUnidad']
        
    comp_nom = users['Comprador']['NombreUnidad']
    comp_dir = users['Comprador']['DireccionUnidad']
    comp_com = users['Comprador']['ComunaUnidad']
    comp_reg = users['Comprador']['RegionUnidad']
    cod_unspsc = listado[0]['Items']['Listado'][0]['CodigoCategoria']
    nom_unspsc = listado[0]['Items']['Listado'][0]['Categoria']
    
else:
    pass




