from django.db import models

# Create your models here.
class Providers(models.Model):
    register_id = models.AutoField(primary_key=True, verbose_name="id de registro")
    description = models.CharField(max_length=200, verbose_name="razón social")
    rfc = models.CharField(max_length=30, verbose_name="Número de RFC")
    address = models.CharField(max_length=200, verbose_name="dirección")
    category = models.CharField(max_length=50, verbose_name="Categoría")
    phone = models.CharField(max_length=50, verbose_name="número telefónico")
    email = models.EmailField(verbose_name="correo electrónico")
    registered = models.DateTimeField(auto_now_add=True, verbose_name="fecha de registro")
    
    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"
        ordering = ['description']
     
    def __str__(self):
        return (self.description)

    
