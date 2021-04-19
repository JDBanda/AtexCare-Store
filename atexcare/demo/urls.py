from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_views
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
    path('usuario_history', views.user_history, name='user_history'),
    # Pedir que se actualice la contraseña
    path('reset_password/',
         auth_views.PasswordResetView.as_view(
             template_name='demo/password_reset.html'),
         name='password_reset'),
    # Se confirma que se ha enviado un correo
    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='demo/password_reset_done.html'),
         name='password_reset_done'),
    # Plantilla del correo
    path('reset/<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='demo/password_reset_confirm.html'),
         name='password_reset_confirm'),
    # Página para cambiar pass
    path('reset_password_complete',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='demo/password_change_done.html'),
         name='password_change_done'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
