from django.db import models
from django.contrib.auth.models import User
from customer.models import Customer

class Compania(models.Model):
    compania_name =models.CharField(max_length=200)
    creation_date =models.DateField(auto_now=True)
    def __str__(self):
        return self.compania_name

class Moneda(models.Model):
    moneda_name =models.CharField(max_length=200)
    creation_date =models.DateField(auto_now=True)
    def __str__(self):
        return self.moneda_name

class Category(models.Model):
    category_name =models.CharField(max_length=100)
    creation_date =models.DateField(auto_now=True)
    def __str__(self):
        return self.category_name

class Policy(models.Model):
    category= models.ForeignKey('Category', on_delete=models.CASCADE)
    policy_name=models.CharField(max_length=200)
    sum_assurance=models.PositiveIntegerField()
    premium=models.PositiveIntegerField()
    tenure=models.PositiveIntegerField()
    creation_date =models.DateField(auto_now=True)
    def __str__(self):
        return self.policy_name

class PolicyRecord(models.Model):
    customer= models.ForeignKey(Customer, on_delete=models.CASCADE)
    Policy= models.ForeignKey(Policy, on_delete=models.CASCADE)
    status = models.CharField(max_length=100,default='Pending')
    creation_date =models.DateField(auto_now=True)
    def __str__(self):
        return self.policy

class PolizaRecord(models.Model):
    customer= models.ForeignKey(Customer, on_delete=models.CASCADE)
    policy= models.PositiveIntegerField()
    moneda=models.PositiveIntegerField()
    monto_asegurado=models.PositiveIntegerField()
    glosa=models.CharField(max_length=200)
    vigencia_desde =models.DateField()
    vigencia_hasta =models.DateField()
    rut_unidad=models.CharField(max_length=30)
    nombre_unidad=models.CharField(max_length=100)
    calle_unidad=models.CharField(max_length=100)
    numero_unidad=models.CharField(max_length=100)
    comuna_unidad=models.CharField(max_length=100)
    region_unidad=models.CharField(max_length=100,default='')
    status = models.CharField(max_length=100,default='Pendiente')
    creation_date =models.DateField(auto_now=True)

    def __str__(self):
        return self.policy

class Question(models.Model):
    customer= models.ForeignKey(Customer, on_delete=models.CASCADE)
    description =models.CharField(max_length=500)
    admin_comment=models.CharField(max_length=200,default='Nothing')
    asked_date =models.DateField(auto_now=True)
    def __str__(self):
        return self.description

class PolizaTemp(models.Model):
    CodigoExterno= models.CharField(max_length=30)
    Nombre= models.CharField(max_length=100)
    Descripcion= models.CharField(max_length=300)
    MontoEstimado = models.FloatField(default=0)
    FechaCierre =models.DateField(auto_now=True)
    rut_unidad=models.CharField(max_length=30)
    nombre_unidad=models.CharField(max_length=100)
    calle_unidad=models.CharField(max_length=100)
    numero_unidad=models.CharField(max_length=100)
    comuna_unidad=models.CharField(max_length=100)
    region_unidad=models.CharField(max_length=100,default='')
    codunspsc= models.CharField(max_length=30)
    nomunspsc= models.CharField(max_length=300)

class Spsc(models.Model):
    codunspsc= models.CharField(max_length=30)
    nomunspsc= models.CharField(max_length=300)
    def __str__(self):
        return self.nomunspsc
    @property
    def get_spsc(self):
        return self.customer.spsc

class LiciTemp(models.Model):
    CodigoExterno= models.CharField(max_length=30)