from django.db import models

# Create your models here.
class autor(models.Model):
    nombre = models.CharField(max_length=40)
    apaterno = models.CharField(max_length=25)
    amaterno = models.CharField(max_length=25)
    nacionalidad = models.CharField(max_length=25)
    biografia = models.TextField()
    sexo= models.CharField(choices=(('M','Mujer'),('H','Hombre')), max_length=16,blank=True)
    genero_lit = models.CharField(choices=(('D','Drama'),('T','Terror')),max_length=16)
    edad = models.CharField(max_length=25)
    estado = models.CharField(choices=(('V','Vivo'),('T','Muerto')),max_length=16)
