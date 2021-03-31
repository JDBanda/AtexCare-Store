from django.db import models
# Create your models here.
# Modelo de prueba


class Product (models.Model):

    class Category(models.IntegerChoices):
        CUBREBOCAS = 1
        BATAS = 2
        BOTAS = 3
        GORROS = 4
        INSUMOS = 5

    name = models.CharField("nombre del producto", max_length=50)
    short_description = models.CharField("pequeña descripción", max_length=150)
    long_description = models.CharField("descripción larga", max_length=500)
    price = models.FloatField("precio normal")
    discount = models.FloatField("descuento")
    category = models.IntegerField(choices=Category.choices)
    image = models.ImageField(upload_to='principal_img', null=True)
    stock = models.IntegerField(null=True)

    def __str__(self):
        return self.name


class Feature (models.Model):
    name = models.CharField("Nombre caracteristica", max_length=50)
    feature = models.CharField(
        "Descripcion de la caracteristica", max_length=250)
    product = models.ManyToManyField(Product)

    def __str__(self):
        return self.name
