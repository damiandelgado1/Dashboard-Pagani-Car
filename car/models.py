from django.db import models

# Model with data and characteristics of Car
class Car(models.Model):
    brand = models.CharField(max_length=20, null=True, verbose_name="Marca del Auto")
    model = models.CharField(max_length=20, verbose_name="Modelo")
    motor = models.TextField(verbose_name="Motor")
    dimmenssion = models.IntegerField(verbose_name="Dimensiones del Auto")
    weight = models.DecimalField(max_digits=6, decimal_places=2, null=True, verbose_name="Marca del Auto")
    consumtion = models.IntegerField(verbose_name="Litros de Consumo")
    external_color = models.CharField(max_length=20, null=True, verbose_name="Color exterior")
    internal_color = models.CharField(max_length=20, null=True, verbose_name="Color interior")
    stock = models.IntegerField(verbose_name="Unidades disponibles")
    availability = models.CharField(max_length=20, verbose_name="Disponibilidad del Auto")
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Precio del Auto")

    def __str__(self):
        return f"{self.model} {self.brand}"

    class Meta:
        verbose_name = "car"
        verbose_name_plural = "cars"