"""solutorresseg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path

from insurance import views
from django.contrib.auth.views import LogoutView,LoginView
from django.urls import path,include
from solutorresseg.views import GetDroplets, GetLicita, GetLicita1, GetLicita2, GetLicita3
from customer.views import PartidaConcluida,PartidaDetailView 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', GetDroplets.as_view(template_name='insurance/welcome.html'), name='Droplet View'),
    path('customer/',include('customer.urls')),
    
    path('licitaciones', GetDroplets.as_view(template_name='insurance/licitaciones.html'), name='Licitaciones'),
    path('licitaciones1/<pk>', GetLicita.as_view(template_name='insurance/licitaciones1.html'),name='licitaciones1'),
    path('asegurar1/<pk>', GetLicita1.as_view(template_name='customer/asegurar1.html'),name='asegurar1'),

    path('organismodemandante/<pk>', GetLicita2.as_view(template_name='customer/organismodemandante.html'),name='asegurar1'),
    path('etapas/<pk>', GetLicita3.as_view(template_name='customer/etapas.html'),name='asegurar1'),


    path('ask-question11/<int:pk>/', PartidaDetailView.as_view(), name='partida'),
    path('ask-question1/<int:pk>/vencedores', PartidaConcluida, name='vencedores'),
    path('approve-request1/<pk>', views.approve_request1_view,name='approve-request1'),
    path('',views.home_view,name=''),
    path('logout', LogoutView.as_view(template_name='insurance/logout.html'),name='logout'),
    path('aboutus', views.aboutus_view),
    path('contactus', views.contactus_view),
    path('afterlogin', views.afterlogin_view,name='afterlogin'),

    

    path('adminlogin', LoginView.as_view(template_name='insurance/adminlogin.html'),name='adminlogin'),
    path('admin-dashboard', views.admin_dashboard_view,name='admin-dashboard'),

    path('admin-view-customer', views.admin_view_customer_view,name='admin-view-customer'),
    path('update-customer/<int:pk>', views.update_customer_view,name='update-customer'),
    path('delete-customer/<int:pk>', views.delete_customer_view,name='delete-customer'),

    path('admin-category', views.admin_category_view,name='admin-category'),
    path('admin-view-category', views.admin_view_category_view,name='admin-view-category'),
    path('admin-update-category', views.admin_update_category_view,name='admin-update-category'),
    path('update-category/<int:pk>', views.update_category_view,name='update-category'),
    path('admin-add-category', views.admin_add_category_view,name='admin-add-category'),
    path('admin-delete-category', views.admin_delete_category_view,name='admin-delete-category'),
    path('delete-category/<int:pk>', views.delete_category_view,name='delete-category'),


    path('admin-moneda', views.admin_moneda_view,name='admin-moneda'),
    path('admin-view-moneda', views.admin_view_moneda_view,name='admin-view-moneda'),
    path('admin-update-moneda', views.admin_update_moneda_view,name='admin-update-moneda'),
    path('update-moneda/<int:pk>', views.update_moneda_view,name='update-moneda'),
    path('admin-add-moneda', views.admin_add_moneda_view,name='admin-add-moneda'),
    path('admin-delete-moneda', views.admin_delete_moneda_view,name='admin-delete-moneda'),
    path('delete-moneda/<int:pk>', views.delete_moneda_view,name='delete-moneda'),    



    path('admin-policy', views.admin_policy_view,name='admin-policy'),
    path('admin-add-policy', views.admin_add_policy_view,name='admin-add-policy'),
    path('admin-view-policy', views.admin_view_policy_view,name='admin-view-policy'),
    path('admin-update-policy', views.admin_update_policy_view,name='admin-update-policy'),
    path('update-policy/<int:pk>', views.update_policy_view,name='update-policy'),
    path('admin-delete-policy', views.admin_delete_policy_view,name='admin-delete-policy'),
    path('delete-policy/<int:pk>', views.delete_policy_view,name='delete-policy'),

    path('admin-view-policy-holder', views.admin_view_policy_holder_view,name='admin-view-policy-holder'),
    path('admin-view-approved-policy-holder', views.admin_view_approved_policy_holder_view,name='admin-view-approved-policy-holder'),
    path('admin-view-disapproved-policy-holder', views.admin_view_disapproved_policy_holder_view,name='admin-view-disapproved-policy-holder'),
    path('admin-view-waiting-policy-holder', views.admin_view_waiting_policy_holder_view,name='admin-view-waiting-policy-holder'),
    path('approve-request/<int:pk>', views.approve_request_view,name='approve-request'),
    path('reject-request/<int:pk>', views.disapprove_request_view,name='reject-request'),
    path('admin-question', views.admin_question_view,name='admin-question'),
   
    path('update-question/<int:pk>', views.update_question_view,name='update-question'),
]