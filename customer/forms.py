from django import forms
from django.contrib.auth.models import User
from insurance import models as CMODEL





class CustomerUserForm(forms.ModelForm):

    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }


class CustomerForm(forms.ModelForm):
    
    spsc=forms.ModelChoiceField(queryset=CMODEL.Spsc.objects.all().order_by('nomunspsc'),empty_label="Codigo spsc", to_field_name="codunspsc")
   #### spsc = forms.ModelMultipleChoiceField(queryset=CMODEL.Spsc.objects.all().order_by('nomunspsc'))

    class Meta:
        
        model=CMODEL.Customer

        fields=['address','mobile']
       