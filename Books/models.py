from django.db import models

# Create your models here.
class Book(models.Model):
    titulo = models.CharField(max_length=60)
    autor = models.CharField(max_length=40)
    fecha_publicacion=models.DateField()
    foto_portada=models.URLField()
    descripcion = models.TextField()
    rating = models.DecimalField(max_digits=1, decimal_places=1)
    comentarios=models.TextField()
    genero=models.CharField(choices=(('D','Drama'),('T','Terror')),max_length=16)
