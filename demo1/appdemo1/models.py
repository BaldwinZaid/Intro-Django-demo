from django.db import models

# Create your models here.



class alumno(models.Model):
    
    name = models.CharField(("nombre"), max_length=255)
    mail = models.CharField(('correo'), max_length=255)
    group = models.CharField(('grupo'), max_length=255)
