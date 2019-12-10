from django.db import models

# Create your models here.
def custom_upload_to(instance, filename):
    return f'payments/{ instance.name }_{ instance.lastname }/' + filename

class Payments(models.Model):
    name = models.CharField(max_length=50, verbose_name="nombre")
    lastname = models.CharField(max_length=50, verbose_name="apellido")
    address = models.CharField(max_length=100, verbose_name="dirección")
    description = models.CharField(max_length=200, verbose_name="Descripción del Pago")
    #amount = models.IntegerField(verbose_name="monto del pago")
    amount = models.DecimalField(decimal_places=2, max_digits=20, verbose_name="monto", blank=False, null=False, )
    type_of_payment = models.CharField(max_length=50, verbose_name="tipo de pago")
    proof_of_payment = models.ImageField(upload_to=custom_upload_to, verbose_name="Comprobante de Pago",)
    date_of_payment = models.DateTimeField( verbose_name="fecha de pago")

    class Meta:
        verbose_name = "Pago"
        verbose_name_plural = "Pagos"
        ordering = ['-date_of_payment']
    
    def __str__(self):
        return (self.name + ' ' + self.lastname)
