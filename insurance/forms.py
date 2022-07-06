from django import forms
from django.contrib.auth.models import User
from . import models

class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))


class CategoryForm(forms.ModelForm):
    class Meta:
        model=models.Category
        fields=['category_name']

class MonedaForm(forms.ModelForm):
    class Meta:
        model=models.Moneda
        fields=['moneda_name']

class PolicyForm(forms.ModelForm):
    category=forms.ModelChoiceField(queryset=models.Category.objects.all(),empty_label="Categoria Nombre", to_field_name="id")
    class Meta:
        model=models.Policy
        fields=['policy_name','sum_assurance','premium','tenure']

class QuestionForm(forms.ModelForm):
    class Meta:
        model=models.Question
        fields=['description']
        widgets = {
        'description': forms.Textarea(attrs={'rows': 6, 'cols': 30})
        }



class AsegurarForm(forms.ModelForm):
   policy=forms.ModelChoiceField(queryset=models.Policy.objects.all(),empty_label="Policy Name", to_field_name="id")
   moneda=forms.ModelChoiceField(queryset=models.Moneda.objects.all(),empty_label="Moneda Name", to_field_name="id")
   class Meta:
        model=models.PolizaRecord
        fields=['monto_asegurado','glosa','vigencia_desde','vigencia_hasta']
   
    
class Question1Form(forms.ModelForm):
    policy=forms.ModelChoiceField(queryset=models.Policy.objects.all(),empty_label="Policy Name", to_field_name="id")
    moneda=forms.ModelChoiceField(queryset=models.Moneda.objects.all(),empty_label="Moneda Name", to_field_name="id")
    class Meta:
        model=models.PolizaRecord
        fields=['monto_asegurado','glosa','vigencia_desde','vigencia_hasta','nombre_unidad','calle_unidad','rut_unidad','numero_unidad','comuna_unidad','region_unidad']
           