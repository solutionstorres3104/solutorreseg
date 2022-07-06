import os
import ast
import requests
import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from solutorresseg.services import get_droplets
from solutorresseg.services1 import get_licita2
from django.shortcuts import render,redirect,reverse
from . import forms,models
from django.db.models import Sum
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required,user_passes_test
from django.conf import settings
from datetime import date, timedelta
from django.db.models import Q
from django.core.mail import send_mail
from django.contrib.auth.models import User
from customer import models as CMODEL
from customer import forms as CFORM
from django.contrib.admin.widgets import  AdminDateWidget, AdminTimeWidget, AdminSplitDateTime
from django.http import HttpResponse
from django.template import RequestContext

class GetDroplets(TemplateView):
    template_name = 'index.html'
    paginate_by = 5
    def get_context_data(self):
       context = {
            'droplets' : get_droplets(),
        }
       return context



def home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')  
    return render(request,'insurance/index.html')


def is_customer(user):
    return user.groups.filter(name='CUSTOMER').exists()


def afterlogin_view(request):
    if is_customer(request.user):      
        return redirect('customer/customer-dashboard')
    else:
        return redirect('admin-dashboard')



def adminclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return HttpResponseRedirect('adminlogin')


@login_required(login_url='adminlogin')
def admin_dashboard_view(request):
    dict={
        'total_user':CMODEL.Customer.objects.all().count(),
        'total_policy':models.Policy.objects.all().count(),
        'total_category':models.Category.objects.all().count(),
        'total_question':models.Question.objects.all().count(),
        'total_policy_holder':models.PolizaRecord.objects.all().count(),
        'approved_policy_holder':models.PolizaRecord.objects.all().filter(status='Approved').count(),
        'disapproved_policy_holder':models.PolizaRecord.objects.all().filter(status='Disapproved').count(),
        'waiting_policy_holder':models.PolizaRecord.objects.all().filter(status='Pending').count(),
    }
    return render(request,'insurance/admin_dashboard.html',context=dict)



@login_required(login_url='adminlogin')
def admin_view_customer_view(request):
    customers= CMODEL.Customer.objects.all()
    return render(request,'insurance/admin_view_customer.html',{'customers':customers})



@login_required(login_url='adminlogin')
def update_customer_view(request,pk):
    customer=CMODEL.Customer.objects.get(id=pk)
    user=CMODEL.User.objects.get(id=customer.user_id)
    userForm=CFORM.CustomerUserForm(instance=user)
    customerForm=CFORM.CustomerForm(request.FILES,instance=customer)
    
    mydict={'userForm':userForm,'customerForm':customerForm}
    if request.method=='POST':
        userForm=CFORM.CustomerUserForm(request.POST,instance=user)
        customerForm=CFORM.CustomerForm(request.POST,request.FILES,instance=customer)
        if userForm.is_valid() and customerForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            customerForm.save()
            return redirect('admin-view-customer')
    return render(request,'insurance/update_customer.html',context=mydict)



@login_required(login_url='adminlogin')
def delete_customer_view(request,pk):
    customer=CMODEL.Customer.objects.get(id=pk)
    user=User.objects.get(id=customer.user_id)
    user.delete()
    customer.delete()
    return HttpResponseRedirect('/admin-view-customer')



def admin_category_view(request):
    return render(request,'insurance/admin_category.html')

def admin_add_category_view(request):
    categoryForm=forms.CategoryForm() 
    if request.method=='POST':
        categoryForm=forms.CategoryForm(request.POST)
        if categoryForm.is_valid():
            categoryForm.save()
            return redirect('admin-view-category')
    return render(request,'insurance/admin_add_category.html',{'categoryForm':categoryForm})

def admin_view_category_view(request):
    monedas = models.Category.objects.all()
    return render(request,'insurance/admin_view_category.html',{'monedas':monedas})

def admin_delete_category_view(request):
    monedas = models.Category.objects.all()
    return render(request,'insurance/admin_delete_category.html',{'monedas':monedas})
    
def delete_category_view(request,pk):
    category = models.Category.objects.get(id=pk)
    category.delete()
    return redirect('admin-delete-category')

def admin_update_category_view(request):
    categories = models.Category.objects.all()
    return render(request,'insurance/admin_update_category.html',{'categories':categories})

@login_required(login_url='adminlogin')
def update_category_view(request,pk):
    category = models.Category.objects.get(id=pk)
    categoryForm=forms.CategoryForm(instance=category)
    
    if request.method=='POST':
        categoryForm=forms.CategoryForm(request.POST,instance=category)
        
        if categoryForm.is_valid():

            categoryForm.save()
            return redirect('admin-update-category')
    return render(request,'insurance/update_category.html',{'categoryForm':categoryForm})
  
 
  

def admin_policy_view(request):
    return render(request,'insurance/admin_policy.html')


def admin_add_policy_view(request):
    policyForm=forms.PolicyForm() 
    
    if request.method=='POST':
        policyForm=forms.PolicyForm(request.POST)
        if policyForm.is_valid():
            categoryid = request.POST.get('category')
            category = models.Category.objects.get(id=categoryid)
            
            policy = policyForm.save(commit=False)
            policy.category=category
            policy.save()
            return redirect('admin-view-policy')
    return render(request,'insurance/admin_add_policy.html',{'policyForm':policyForm})

def admin_view_policy_view(request):
    policies = models.Policy.objects.all()
    return render(request,'insurance/admin_view_policy.html',{'policies':policies})



def admin_update_policy_view(request):
    policies = models.Policy.objects.all()
    return render(request,'insurance/admin_update_policy.html',{'policies':policies})

@login_required(login_url='adminlogin')
def update_policy_view(request,pk):
    policy = models.Policy.objects.get(id=pk)
    policyForm=forms.PolicyForm(instance=policy)
    
    if request.method=='POST':
        policyForm=forms.PolicyForm(request.POST,instance=policy)
        
        if policyForm.is_valid():

            categoryid = request.POST.get('category')
            category = models.Category.objects.get(id=categoryid)
            
            policy = policyForm.save(commit=False)
            policy.category=category
            policy.save()
           
            return redirect('admin-update-policy')
    return render(request,'insurance/update_policy.html',{'policyForm':policyForm})
  
  
def admin_delete_policy_view(request):
    policies = models.Policy.objects.all()
    return render(request,'insurance/admin_delete_policy.html',{'policies':policies})
    
def delete_policy_view(request,pk):
    policy = models.Policy.objects.get(id=pk)
    policy.delete()
    return redirect('admin-delete-policy')

def admin_view_policy_holder_view(request):
    policyrecords = models.PolizaRecord.objects.all()
    return render(request,'insurance/admin_view_policy_holder.html',{'policyrecords':policyrecords})

def admin_view_approved_policy_holder_view(request):
    policyrecords = models.PolizaRecord.objects.all().filter(status='Approved')
    return render(request,'insurance/admin_view_approved_policy_holder.html',{'policyrecords':policyrecords})

def admin_view_disapproved_policy_holder_view(request):
    policyrecords = models.PolizaRecord.objects.all().filter(status='Disapproved')
    return render(request,'insurance/admin_view_disapproved_policy_holder.html',{'policyrecords':policyrecords})

def admin_view_waiting_policy_holder_view(request):
    policyrecords = models.PolizaRecord.objects.all().filter(status='Pending')
    return render(request,'insurance/admin_view_waiting_policy_holder.html',{'PolizaRecords':policyrecords})

def approve_request_view(request,pk):
    policyrecords = models.PolizaRecord.objects.get(id=pk)
    policyrecords.status='Aprovada'
    policyrecords.save()
    return redirect('admin-view-policy-holder')

def disapprove_request_view(request,pk):
    policyrecords = models.PolizaRecord.objects.get(id=pk)
    policyrecords.status='Rechazada'
    policyrecords.save()
    return redirect('admin-view-policy-holder')



def admin_question_view(request):
    questions = models.Question.objects.all()
    return render(request,'insurance/admin_question.html',{'questions':questions})

def update_question_view(request,pk):
    question = models.Question.objects.get(id=pk)
    questionForm=forms.QuestionForm(instance=question)
    
    if request.method=='POST':
        questionForm=forms.QuestionForm(request.POST,instance=question)
        
        if questionForm.is_valid():

            admin_comment = request.POST.get('admin_comment')
            
            
            question = questionForm.save(commit=False)
            question.admin_comment=admin_comment
            question.save()
           
            return redirect('admin-question')
    return render(request,'insurance/update_question.html',{'questionForm':questionForm})







def aboutus_view(request):
    return render(request,'insurance/aboutus.html')

def contactus_view(request):
    sub = forms.ContactusForm()
    if request.method == 'POST':
        sub = forms.ContactusForm(request.POST)
        if sub.is_valid():
            email = sub.cleaned_data['Email']
            name=sub.cleaned_data['Name']
            message = sub.cleaned_data['Message']
            send_mail(str(name)+' || '+str(email),message,settings.EMAIL_HOST_USER, settings.EMAIL_RECEIVING_USER, fail_silently = False)
            return render(request, 'insurance/contactussuccess.html')
    return render(request, 'insurance/contactus.html', {'form':sub})




def admin_moneda_view(request):
    return render(request,'insurance/admin_moneda.html')

def admin_add_moneda_view(request):
    monedaForm=forms.MonedaForm() 
    if request.method=='POST':
        monedaForm=forms.MonedaForm(request.POST)
        if monedaForm.is_valid():
            monedaForm.save()
            return redirect('admin-view-moneda')
    return render(request,'insurance/admin_add_moneda.html',{'monedaForm':monedaForm})

def admin_view_moneda_view(request):
    monedas = models.Moneda.objects.all()
    return render(request,'insurance/admin_view_moneda.html',{'monedas':monedas})

def admin_delete_moneda_view(request):
    monedas = models.Moneda.objects.all()
    return render(request,'insurance/admin_delete_moneda.html',{'monedas':monedas})
    
def delete_moneda_view(request,pk):
    moneda = models.Moneda.objects.get(id=pk)
    moneda.delete()
    return redirect('admin-delete-moneda')

def admin_update_moneda_view(request):
    monedas = models.Moneda.objects.all()
    return render(request,'insurance/admin_update_moneda.html',{'monedas':monedas})

@login_required(login_url='adminlogin')

def update_moneda_view(request,pk):
    moneda = models.Moneda.objects.get(id=pk)
    monedaForm=forms.MonedaForm(instance=moneda)
    
    if request.method=='POST':
        monedaForm=forms.MonedaForm(request.POST,instance=moneda)
        
        if monedaForm.is_valid():

            monedaForm.save()
            return redirect('admin-update-moneda')
    return render(request,'insurance/update_moneda.html',{'monedaForm':monedaForm})

def approve_request1_view(request, pk):
    
    url1 = 'http://api.mercadopublico.cl/servicios/v1/publico/licitaciones.json?codigo='
    url2 = pk
    url3 = '&ticket=F8537A18-6766-4DEF-9E59-426B4FEE2844'
    url = url1+url2+url3
     
    response = requests.get(url)
    if response.status_code ==200:
        licitas = response.json()
        listado = licitas['Listado']
        users = listado[0]
       
        
        context = {
            'users' : users,
            
        }
        
        address = users['CodigoExterno']
        address = str(address)
        print("address")
        date_assign = str(date.today())
        address = date_assign
        
        return render(request,'customer/ask-question1.html',{'users':users})
        return redirect('/customer/ask-question1',{'address11':address})
        return redirect('/customer/ask-question1',{'users':users})
        
       
        

        

        