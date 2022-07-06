from django.shortcuts import render
from django.views.generic import TemplateView
from .services import get_droplets,get_droplets2
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .services1 import get_licita


class GetDroplets(TemplateView):
    ####list = get_droplets2()
    
    ####paginate_by = 5
    listados = get_droplets()
    
    ####paginator = Paginator(listados, paginate_by)
    ####page_num=  1
    ####page_obj = paginator.get_page(page_num)
    template_name = 'licitaciones.html'
	
    
    def get_context_data(self):
       order_by = self.kwargs.get('order_by') or 'Nombre'
       context = {
            'listados' : get_droplets(),
        }
       return context



class GetLicita(TemplateView):
    template_name = 'licitaciones1.html'
    def get_context_data(request,pk):
       context = {
            'users' : get_licita(pk),
        }
       
       return context

class GetLicita1(TemplateView):
    template_name = 'customer/asegurar1.html'
    def get_context_data(request,pk):
       context = {
            'users' : get_licita(pk),
        }
       
       return context


class GetLicita2(TemplateView):
    template_name = 'customer/organismodemandante.html'
    def get_context_data(request,pk):
       context = {
            'users' : get_licita(pk),
        }
       
       return context

class GetLicita3(TemplateView):
    template_name = 'customer/etapas.html'
    def get_context_data(request,pk):
       context = {
            'users' : get_licita(pk),
        }
       
       return context