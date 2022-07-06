from math import trunc
from insurance.models import PolizaTemp
from django.shortcuts import get_object_or_404


def contextVencedores(pk):
    
    polizaTemp = get_object_or_404(PolizaTemp, pk=pk)
        
    codigo_externo=polizaTemp.CodigoExterno
    comp_rut = polizaTemp.rut_unidad
    comp_nom = polizaTemp.nombre_unidad
    comp_dir = polizaTemp.calle_unidad
    comp_com = polizaTemp.comuna_unidad
    comp_reg = polizaTemp.region_unidad
    cod_unspsc = polizaTemp.codunspsc
    nom_unspsc = polizaTemp.nomunspsc
    
    
        
    context = {
        
        'codigo_externo': codigo_externo,
        'comp_rut':comp_rut,
        'comp_nom':comp_nom,
        'comp_dir':comp_dir,
        'comp_com':comp_com,
        'comp_reg':comp_reg,
        'cod_unspsc':cod_unspsc,
        'nom_unspsc':nom_unspsc,
    }
    print(context)
    return context 

def contextLicita(pk):
    
    polizaTemp = get_object_or_404(PolizaTemp, pk=pk)
        
    codigo_externo=polizaTemp.CodigoExterno
    comp_rut = polizaTemp.rut_unidad
    comp_nom = polizaTemp.nombre_unidad
    comp_dir = polizaTemp.calle_unidad
    comp_com = polizaTemp.comuna_unidad
    comp_reg = polizaTemp.region_unidad
    cod_unspsc = polizaTemp.codunspsc
    nom_unspsc = polizaTemp.nomunspsc
    
    
        
    context = {
        
        'codigo_externo': codigo_externo,
        'comp_rut':comp_rut,
        'comp_nom':comp_nom,
        'comp_dir':comp_dir,
        'comp_com':comp_com,
        'comp_reg':comp_reg,
        'cod_unspsc':cod_unspsc,
        'nom_unspsc':nom_unspsc,
    }
    print(context)
    return context 