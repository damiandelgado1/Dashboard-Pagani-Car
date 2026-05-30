from django.db import models

# Model with data and characteristics of Car
class Car(models.Model):
    brand = models.CharField(max_length=20, null=True, verbose_name="Marca del Auto")
    model = models.CharField(max_length=20, verbose_name="Modelo")
    photo = models.ImageField(upload_to="car/", blank=True, verbose_name="Foto del Auto")
    preview = models.TextField(verbose_name="Previsualizacion Auto")
    description = models.TextField(verbose_name="Descripcion")
    photo_interior = models.ImageField(upload_to="interior_car/", blank=True, verbose_name="Fotos de Interior del Auto")
    tires = models.CharField(max_length=20, verbose_name="Dimensiones del Auto")
    max_speed = models.DecimalField(max_digits=6, decimal_places=2, null=True, verbose_name="Peso")
    tire = models.CharField(max_length=30, verbose_name="Litros de Consumo")
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