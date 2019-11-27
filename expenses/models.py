from django.db import models
import datetime

# Create your models here.
class Expenses(models.Model):
    date = models.DateField(verbose_name="fecha")
    folio = models.CharField(max_length=50, verbose_name="folio")
    provider = models.CharField(max_length=200, verbose_name="proveedor")
    description = models.CharField(max_length=200, verbose_name="descripción")
    notes = models.CharField(max_length=300, verbose_name="observaciones adicionales")

    class Meta:
        verbose_name = "Gasto"
        verbose_name_plural = "Gastos"
        ordering = ['-date']
     
    def __str__(self):
        return (self.folio + ' : ' + self.description)

    

