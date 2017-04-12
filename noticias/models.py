from django.db import models

class Noticia(models.Model):
    nombre = models.CharField(blank=True, max_length=100)
    descripcion = models.TextField(blank=True)
    
    def __str__(self):
        return self.nombre
