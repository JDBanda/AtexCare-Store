from django.db import models
# User de Django
from django.contrib.auth.models import User
# Signals
from django.db.models.signals import post_save
from django.dispatch import receiver

# Producto base


class Product (models.Model):
    name = models.CharField("nombre del producto", max_length=50)
    short_description = models.CharField("pequeña descripción", max_length=150)
    long_description = models.CharField("descripción larga", max_length=500)
    price = models.FloatField("precio normal")
    discount = models.FloatField("descuento")
    image = models.ImageField(upload_to='principal_img', null=True)
    stock = models.IntegerField(null=True)

    def __str__(self):
        return self.name

# Características, una característicica puede estar en varios productos


class Feature (models.Model):
    name = models.CharField("Nombre caracteristica", max_length=50)
    feature = models.CharField(
        "Descripcion de la caracteristica", max_length=250)
    product = models.ManyToManyField(Product)

    def __str__(self):
        return self.name

# Extiende de users, pero son datos adicionales que sirven para el perfil


class Profile (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tel_1 = models.CharField(
        "Teléfono o número de celular", null=True, max_length=10)
    # Datos de facturación
    razon_social = models.CharField(
        "Razón social", null=True, blank=True, max_length=150)
    rfc = models.CharField("RFC", null=True, blank=True, max_length=50)
    direccion_fiscal = models.CharField(
        "Dirección fiscal", null=True, blank=True, max_length=250)
    ciudad = models.CharField("Ciudad", null=True, blank=True, max_length=50)
    estado_fact = models.CharField(
        "Estado", null=True, blank=True, max_length=50)
    tel_2 = models.CharField("Teléfono de facturación",
                             null=True, blank=True, max_length=50)
    correo_fact = models.EmailField(
        "Correo de facturación", null=True, blank=True, max_length=254)
    cfdi = models.CharField("CFDI", null=True, blank=True, max_length=50)
    # Datos de envío
    direccion = models.CharField(
        "Dirección", null=True, blank=True, max_length=50)
    municipio = models.CharField(
        "Municipio", null=True, blank=True, max_length=50)
    estado = models.CharField("Estado", null=True, blank=True, max_length=50)
    cp = models.CharField("Código Postal", null=True, blank=True, max_length=6)
    numero_ext = models.IntegerField("Número exterior", null=True, blank=True)
    numero_int = models.IntegerField("Número interior", null=True, blank=True)
    entre_calle = models.CharField(
        "Entre calle", null=True, blank=True, max_length=50)
    entre_calle_2 = models.CharField(
        "Y calle", null=True, blank=True, max_length=50)

    def __str__(self):
        return "perfil de: " + self.user.username


class Carrito(models.Model):
    PAGADO = 0
    ACTIVO = 1

    STATUS_CHOICES = (
        ("PAGADO", PAGADO),
        ("ACTIVO", ACTIVO),
    )

    producto = models.ForeignKey(Product, on_delete=models.CASCADE)
    cantidad = models.IntegerField("Cantidad")
    monto = models.FloatField("Monto")
    usuario = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS_CHOICES, default=ACTIVO)

    def __str__(self):
        return self.usuario.username + ", " + self.producto.name + ", " + str(self.status)


class Compra(models.Model):
    renglonCarrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
