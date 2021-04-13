from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('productos', views.products, name='productos'),
    path('productos/<str:pk>', views.product, name='producto'),
    path('quienes_somos', views.who, name='quienes'),
    path('legal', views.legal, name='legal'),
    path('contacto', views.contact_info, name='contacto'),

    path('detalle_carrito', views.detail_car, name='detalle_carrito'),
    path('detalle_carrito/eliminar', views.delete_car_item, name='eliminarItem'),


    path('envio', views.sending_info, name='envio'),
    path('registro', views.register, name='registro'),
    path('inicio_sesion', views.loginInto, name='login'),
    path('cerrar_sesion', views.logoutInto, name='logout'),
    path('usuario', views.user_profile, name='user'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
