from django.contrib import admin
from .models import *
# Acciones


@admin.action(description="Marcar como compra entregada")
def compra_entregada(modeladmin, request, queryset):
    # Obtener el id de compra
    idCompra = request.POST['_selected_action']
    # Buscar todos los carritos con compra de ese ID y que esten "PAGADOS"
    arrCarritos = Carrito.objects.filter(
        status=status_choices.PAGADO, compra=idCompra)
    # Agarrar la cantidad de cada carro
    try:
        for c in arrCarritos:
            Producto = Product.objects.get(id=c.producto.id)
            Producto.stock = Producto.stock - c.cantidad
            Producto.save()
        # Update al estado de la compra
        queryset.update(status_compra=status_choices.ENTREGADO)
        # Si existe una manera de medir ganancias o así, de aquí se pueden sacar
    except:
        print("No jaló, parece que el stock se actualizó")


class CompraAdmin(admin.ModelAdmin):
    list_display = ['fecha_compra', 'status_compra',
                    'usuario', 'total', 'paqueteria']
    ordering = ['fecha_compra']
    actions = [compra_entregada]


# Register your models here.
admin.site.register(Product)
admin.site.register(Feature)
admin.site.register(Profile)
admin.site.register(Carrito)
admin.site.register(Image_collection)
admin.site.register(Compra, CompraAdmin)
