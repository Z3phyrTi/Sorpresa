
from enum import Flag
from django.db import models
from django.forms import widgets
from django import forms

# Create your models here.

class Nota(models.Model):
    titulo_nota = models.CharField('titulo nota',
     max_length= 50,
     blank= False,
     null= False
     ) 
    descripcion_nota = models.CharField('descripcion nota',
        max_length= 200,
        blank= False,
        null= False,
        default= 0
    )     

    fecha_creacion = models.DateTimeField('Fecha de creacion',
        auto_now= True
    )

    fecha_limite = models.DurationField('Fecha Limite',
    default= 0

    )   
