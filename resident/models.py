from django.db import models

# Create your models here.
class Resident(models.Model):
    name = models.CharField(max_length=50, verbose_name="nombre")
    lastname = models.CharField(max_length=50, verbose_name="apellido")
    address = models.CharField(max_length=100, verbose_name="dirección")
    email = models.EmailField(verbose_name="correo electrónico")
    type_of_property = models.CharField(max_length=50, verbose_name="tipo de inmueble")
    owner_name = models.CharField(max_length=100, verbose_name="nombre del propietario")

    def __str__(self):
        return (self.name + ' ' + self.lastname)

    

