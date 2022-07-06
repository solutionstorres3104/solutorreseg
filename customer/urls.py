from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from .views import PartidaConcluida 
                
app_name = 'customer'                   
                    

urlpatterns = [
    path('customerclick', LoginView.as_view(template_name='customer/customerclick.html'),name='customerclick'),

    
    path('customersignup', views.customer_signup_view,name='customersignup'),
    path('customer-dashboard', views.customer_dashboard_view,name='customer-dashboard'),
    path('customerlogin', LoginView.as_view(template_name='insurance/adminlogin.html'),name='customerlogin'),

    path('apply-policy', views.apply_policy_view,name='apply-policy'),
    path('apply/<int:pk>', views.apply_view,name='apply'),
    path('history', views.history_view,name='history'),
    path('asegurar', views.asegurar_view,name='asegurar'),


    
    path('asegurar11/<pk>', views.asegurar11_view,name='asegurar11'),
    path('asegurar2/<pk>', views.asegurar2_view,name='asegurar2'),
    path('ask-question', views.ask_question_view,name='ask-question'),
    path('ask-question1', views.ask_question1_view,name='ask-question1'),
    path('ask-question1/<pk>/vencedores', PartidaConcluida, name='vencedores'),
    path('question-history', views.question_history_view,name='question-history'),
    path('question1-history', views.question1_history_view,name='question1-history'),
]