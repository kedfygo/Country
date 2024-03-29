from django.db import models


# Create your models here.
class Residents(models.Model):
    name = models.CharField(max_length=50, verbose_name="nombre")
    lastname = models.CharField(max_length=50, verbose_name="apellido")
    address = models.CharField(max_length=100, verbose_name="dirección")
    phone_number = models.CharField(max_length=10, verbose_name="número telefónico", blank=True)
    email = models.EmailField(verbose_name="correo electrónico")
    type_of_property = models.CharField(max_length=50, verbose_name="tipo de inmueble")
    owner_name = models.CharField(max_length=100, verbose_name="nombre del propietario")
    owner_phone_number = models.CharField(max_length=10, verbose_name="número telefónico del propietario", blank=True)

    class Meta:
        verbose_name = "Residente"
        verbose_name_plural = "Residentes"
        ordering = ['-lastname']
     
    def __str__(self):
        return (self.name + ' ' + self.lastname)

    

