import os
import requests
from django.core.paginator import Paginator
from datetime import date
from datetime import datetime
from insurance import models as CMODEL
from insurance.models import LiciTemp,PolizaTemp,Spsc
from customer import models 

currentdate = date.today()
formatDate = currentdate.strftime("%d%m%Y") 
##formatDate = '24062022'
def get_droplets():
    
    url1 = 'https://api.mercadopublico.cl/servicios/v1/publico/licitaciones.json?fecha='
    url2 = formatDate
    url3 = '&estado=publicada&ticket=F8537A18-6766-4DEF-9E59-426B4FEE2844'
    url = url1+url2+url3
    url = 'http://api.mercadopublico.cl/servicios/v1/publico/licitaciones.json?estado=activas&ticket=F8537A18-6766-4DEF-9E59-426B4FEE2844'
    response = requests.get(url)
    if response.status_code ==200:
        content = response.content
        #file = open('licitaciones.html','wb')
        #file.write(content)

    
        droplets = response.json()
             
        listados = droplets['Listado']
        
        lici = listados[0]
        address = lici['CodigoExterno']
        
        
        return listados

def get_droplets2():
    categories = LiciTemp.objects.all()
    for lisis in categories:
            licita = lisis.CodigoExterno
               
            url1 = 'http://api.mercadopublico.cl/servicios/v1/publico/licitaciones.json?codigo='
            url2 = licita
            url3 = '&ticket=F8537A18-6766-4DEF-9E59-426B4FEE2844'
            url = url1+url2+url3
            response = requests.get(url)
            if response.status_code ==200:
                content = response.content
                licitas = response.json()
                listado = licitas['Listado']
                users = listado[0]
                address = users['Nombre']
                codigo_externo=(users["CodigoExterno"])
                nom= (users["Nombre"])
                des= (users["Nombre"])
                monto = (users["MontoEstimado"])
                fecha =(users["FechaCierre"])
                comp_rut = (users['Comprador']['RutUnidad'])
                comp_nom = (users['Comprador']['NombreUnidad'])
                comp_dir = (users['Comprador']['DireccionUnidad'])
                comp_com = (users['Comprador']['ComunaUnidad'])
                comp_reg = (users['Comprador']['RegionUnidad'])
                cod_unspsc = listado[0]['Items']['Listado'][0]['CodigoCategoria']
                nom_unspsc = listado[0]['Items']['Listado'][0]['Categoria']
                registros = PolizaTemp.objects.filter(CodigoExterno=licita).exists()

                if registros < 1 :   
                    datainsertion = CMODEL.PolizaTemp(CodigoExterno=codigo_externo,Nombre=nom,Descripcion=des,MontoEstimado=monto,FechaCierre=fecha,rut_unidad = comp_rut, nombre_unidad = comp_nom, calle_unidad = comp_dir,numero_unidad= address,comuna_unidad=comp_com,region_unidad=comp_reg,codunspsc=cod_unspsc,nomunspsc=nom_unspsc)
                  
                   
                    datainsertion.save()

                    registros = Spsc.objects.filter(codunspsc=cod_unspsc).exists()

                    if registros < 1 :   
                        datainsertion = CMODEL.Spsc(codunspsc=cod_unspsc,nomunspsc=nom_unspsc)
                        datainsertion.save()
 
def get_droplets3(request):
    spsc=models.Customer.objects.get(user_id=request.user.id)
    questions = PolizaTemp.objects.filter(codunspsc=spsc).values()
    totApostas = questions.count()
    print(totApostas)
    
    print(questions)
    return questions