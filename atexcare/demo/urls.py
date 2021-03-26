from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('productos/', views.products, name='productos'),
    path('productos/N', views.product, name='producto'),
    path('quienes_somos', views.who, name='quienes'),
    path('legal', views.legal, name='legal'),
    path('contacto', views.contact_info, name='contacto'),
    path('detalle_carrito', views.detail_car, name='detalle_carrito'),
    path('envio', views.sending_info, name='envio'),
    path('registro', views.register, name='registro'),
    path('inicio_sesion', views.login, name='login'),
    path('usuario/x', views.user, name='user'),
]
