import os
import requests
import json

from insurance import models as CMODEL
###from customer import models as customer
from insurance.models import PolizaTemp, Spsc





def get_licita(licita):
    
    url1 = 'http://api.mercadopublico.cl/servicios/v1/publico/licitaciones.json?codigo='
    
    
    
    ###for lisis in categories:
    ###  licita = lisis.CodigoExterno
      
    url2 = licita
    
    url3 = '&ticket=F8537A18-6766-4DEF-9E59-426B4FEE2844'
    url = url1+url2+url3
    
    
    response = requests.get(url)
    if response.status_code ==200:
      
        ###user=CMODEL.User.objects.get(id=customer.user_id)
        content = response.content
        #file = open('licitaciones.html','wb')
        #file.write(content)
        licitas = response.json()
        listado = licitas['Listado']
        users = listado[0]
        address = users['Nombre']
        codigo_externo=(users["CodigoExterno"])
        comp_rut = users['Comprador']['RutUnidad']
        
        comp_nom = users['Comprador']['NombreUnidad']
        comp_dir = users['Comprador']['DireccionUnidad']
        comp_com = users['Comprador']['ComunaUnidad']
        comp_reg = users['Comprador']['RegionUnidad']
        cod_unspsc = listado[0]['Items']['Listado'][0]['CodigoCategoria']
        nom_unspsc = listado[0]['Items']['Listado'][0]['Categoria']
        content = response.content
        jsondecoded = json.loads(content)
       

        for entity in jsondecoded["Listado"]:
          entityFechas = entity["Fechas"]

       
        xFechaPublicaciont = str(entityFechas['FechaPublicacion']) 
        registros = PolizaTemp.objects.all().count()
        print("get_licita")

  

#Existe el producto Spsc
        registros = PolizaTemp.objects.filter(CodigoExterno=licita).exists()

        if registros < 1 :   
          datainsertion = CMODEL.PolizaTemp(CodigoExterno=codigo_externo,rut_unidad = comp_rut, nombre_unidad = comp_nom, calle_unidad = comp_dir,numero_unidad= address,comuna_unidad=comp_com,region_unidad=comp_reg,codunspsc=cod_unspsc,nomunspsc=nom_unspsc)
          datainsertion.save()

        registros = Spsc.objects.filter(codunspsc=cod_unspsc).exists()

        if registros < 1 :   
          datainsertion = CMODEL.Spsc(codunspsc=cod_unspsc,nomunspsc=nom_unspsc)
          datainsertion.save()
        
        return users

def get_licita1(licita):
    
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
        

        content = response.content
        jsondecoded = json.loads(content)
       

        for entity in jsondecoded["Listado"]:
          entityFechas = entity["Fechas"]

       
        xFechaPublicaciont = str(entityFechas['FechaPublicacion']) 
        
 
       
        return users        

def get_licita2(licita):
    
    url1 = 'http://api.mercadopublico.cl/servicios/v1/publico/licitaciones.json?codigo='
    url2 = licita
    url3 = '&ticket=F8537A18-6766-4DEF-9E59-426B4FEE2844'
    url = url1+url2+url3
    
    
    response = requests.get(url)
    if response.status_code ==200:
        licitas = response.json()
        listado = licitas['Listado']
        users = listado[0]
            
        return users        
    else:
      pass