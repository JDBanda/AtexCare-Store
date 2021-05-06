from django.shortcuts import render, redirect
from .models import *
from .filters import *
from .forms import *
# Mostrar mensajes dado un proceso
from django.contrib import messages
# Autenticar y loggear
from django.contrib.auth import authenticate, login, logout
# Rollback si algo sale mal
from django.db import transaction
# Solicitar inicio de sesion
from django.contrib.auth.decorators import login_required
# Importar json response
from django.http import JsonResponse
# Envío de correos
from django.core.mail import BadHeaderError, send_mail
# Configuraciones
from django.conf import settings
# Fecha
import datetime
# JSON para decodificar
import json


def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        message = request.POST['message']  # Titutlo del email
        email = request.POST['email']
        textarea = request.POST['textarea']
        # Crear un mensaje predeterminado
        textarea = "Nombre: " + name + "\n" + textarea
        try:
            send_mail(
                message,
                textarea,
                email,
                # El mail de quien recibe va en una lista
                [settings.EMAIL_HOST_USER],
                fail_silently=False)
        except BadHeaderError:
            messages.info(
                request, 'Parece que hubo un problema al enviar el correo')
        # Página de exito o mensaje
        messages.info(request, '¡Su mensaje ha sido envíado con exito!')
    context = {}
    return render(request, 'demo/index.html', context)


def products(request):
    # Filtrar los productos
    lista = ProductFilter(request.GET, queryset=Product.objects.all())
    # Tamaño del queryset
    tam = len(lista.qs)
    context = {
        "productos": lista,
        "tam": tam,
    }
    return render(request, 'demo/products.html', context)


def product(request, pk):
    instance = Product.objects.get(id=pk)
    # Obtener de many to many
    b = Image_collection.objects.filter(producto=pk)
    a = Feature.objects.filter(product=pk)
    context = {
        'producto': instance,
        'caracteristicas': a,
        'imagenes': b,
    }
    if request.method == 'POST':
        # Recibimos los datos
        producto = Product.objects.get(id=request.POST.get('producto'))
        cantidad = request.POST.get('cantidad')
        monto = request.POST.get('monto')
        usuario = request.POST.get('usuario')
        # Al hacer post verificar que el ususario este dado de alta
        if usuario == 'AnonymousUser':
            return JsonResponse({
                'content': {
                    'title': 'No ha iniciado sesión',
                    'mensaje': 'Por favor inicie su sesión, claro que debes de estar registrado antes',
                    'url': '/inicio_sesion',
                    'boton': '<i class="bx bx-user-circle"></i> Iniciar sesion',
                    'icon': 'error',
                    'state': True,
                }
            })
        try:
            # Validar si hay un carrito
            usuario = User.objects.get(username=usuario)
            exist = Carrito.objects.get(
                producto=producto, usuario=usuario, status=status_choices.ACTIVO)
            exist.delete()
        except:
            usuario = User.objects.get(username=usuario)
        # Intentar guardar, pues no hay un carrito
        objCarrito = Carrito(
            producto=producto, cantidad=cantidad, monto=monto, usuario=usuario)
        objCarrito.save()
        return JsonResponse({
            'content': {
                'title': '¡Agregado!',
                'url': '/detalle_carrito',
                'boton': '<i class="bx bxs-cart bx-tada"></i> Ver Carrito',
                'icon': 'success',
                'status': True,
            }
        })
    return render(request, 'demo/product.html', context)


def who(request):
    context = {}
    return render(request, 'demo/who.html', context)


def legal(request):
    context = {}
    return render(request, 'demo/legal.html', context)


def contact_info(request):
    context = {}
    return render(request, 'demo/contact_info.html', context)

# Operaciones en el carrito de compras

# Verificar si el usuario tiene los datos de facturación


def check_factura(request):
    profile = Profile.objects.get(user=request.user)
    return JsonResponse({
        'factura': {
            'razon_social': profile.razon_social,
            'rfc': profile.rfc,
            'direccion_fiscal': profile.direccion_fiscal,
            'ciudad': profile.ciudad,
            'estado_fact': profile.estado_fact,
            'tel_2': profile.tel_2,
            'correo_fact': profile.correo_fact,
            'cfdi': profile.cfdi,
        }
    })

# Verificar si el usuario tiene bien los datos de envio


def check_profile(request):
    profile = Profile.objects.get(user=request.user)
    return JsonResponse({
        'profile': {
            'direccion': profile.direccion,
            'municipio': profile.municipio,
            'estado': profile.estado,
            'cp': profile.cp,
            'numero_ext': profile.numero_ext,
            'numero_int': profile.numero_int,
            'entre_calle': profile.entre_calle,
            'entre_calle_2': profile.entre_calle_2,
        }
    })

# Verificar cuantos productos lleva el usuario


def get_car(request):
    cart_count = len(Carrito.objects.filter(
        usuario=request.user, status=status_choices.ACTIVO))
    return JsonResponse({
        'content': {
            'title': 'Objetos en carrito',
            'obj': cart_count,
        }
    })

# Generar orden de compra (Guardar registro de compra y actualizar datos de los renglones del carrito)


def generarOrden(request):
    if request.method == 'POST':
        # Recuperar datos del POST
        usuario = User.objects.get(username=request.POST['usuario'])
        total = request.POST['total']
        paqueteria = request.POST['paqueteria']
        fecha_compra = datetime.datetime.now()
        '''
        datetime(
            request.POST['year'],
            request.POST['month'],
            request.POST['day'],
            request.POST['hour'],
            request.POST['minute'],
            request.POST['second'],
            request.POST['milisec'],
        )
        '''
        # Insertar una Compra
        objCompra = Compra(
            usuario=usuario,
            total=total,
            paqueteria=paqueteria,
            fecha_compra=fecha_compra,)
        objCompra.save()
        # Obtener los ID de carritos
        carrito = request.POST['carrito']
        carrito = json.loads(carrito)
        # Buscar por ID y cambiar valores
        i = 0
        while i < len(carrito):
            objCarrito = Carrito.objects.get(id=carrito[i])
            objCarrito.status = status_choices.PAGADO
            objCarrito.compra = Compra.objects.latest("id")
            objCarrito.save()
            i += 1
        return JsonResponse({
            'content': {
                'title': 'Orden generada',
                'icon': 'success',
            }
        })


@login_required(login_url='login')
def detail_car(request):
    if request.method == 'POST':
        idItem = request.POST['id']
        cantidadItem = request.POST['cantidad']
        montoItem = request.POST['monto']
        objCar = Carrito.objects.get(id=idItem)
        objCar.cantidad = cantidadItem
        objCar.monto = montoItem
        try:
            objCar.save()
            return JsonResponse({
                'content': {
                    'title': '¡Actualizado!',
                    'icon': 'success',
                    'status': True,
                }
            })
        except:
            return JsonResponse({
                'content': {
                    'title': 'Ocurrio un error, intentalo de nuevo',
                    'icon': 'error',
                    'status': False,
                }
            })
    objCar = Carrito.objects.filter(
        usuario=request.user, status=status_choices.ACTIVO)
    # total de articulos
    tObjetos = len(objCar)
    context = {'objetos': objCar, 'totalArticulos': tObjetos}
    return render(request, 'demo/detail_car.html', context)


@login_required(login_url='login')
def delete_car_item(request):
    # Comprobar si es POST
    if request.method == 'POST':
        # Obtener el ID de POST
        idItem = request.POST['id']
        # Obtener el elemento con ese ID
        item = Carrito.objects.get(id=idItem)
        nombre = item.producto.name
        try:
            # Eliminar
            item.delete()
            # Mandar un mensaje
            return JsonResponse({
                'content': {
                    'title': 'Elemento ' + nombre + ' eliminado',
                    'icon': 'success',
                    'status': True,
                }
            })
        except:
            # Mandar mensaje
            return JsonResponse({
                'content': {
                    'title': 'Ocurrió un problema al eliminar, vuelva a intentar',
                    'icon': 'error',
                    'status': False,
                }
            })


def sending_info(request):
    context = {}
    return render(request, 'demo/sending_info.html', context)


def loginInto(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        # Si el usuario no es null pues
        print(user)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/productos')
            else:
                messages.info(
                    request, 'El usuario esta dado de baja')
        else:
            messages.info(
                request, 'El usuario y/o contraseña son erroneos o no están registrados')
    context = {}
    return render(request, 'demo/login.html', context)


def logoutInto(request):
    logout(request)
    messages.info(request, 'Has cerrado la sesión')
    return redirect('/inicio_sesion')


@transaction.atomic
def register(request):
    userForm = UserForm()
    profileForm = ProfileForm()
    if request.method == 'POST':
        userForm = UserForm(request.POST)
        profileForm = ProfileForm(request.POST)
        if userForm.is_valid() and profileForm.is_valid():
            # Se utilza esta forma de guardado debido a que la contraseña se cifra
            # Si usara save() no se puede autenticar correctamente debido al modo de login por defecto de django que descifra la contraseña
            user = User.objects.create_user(
                username=userForm.cleaned_data.get('username'),
                password=userForm.cleaned_data.get('password'),
                email=userForm.cleaned_data.get('email'),
                first_name=userForm.cleaned_data.get('first_name'),
                last_name=userForm.cleaned_data.get('last_name'),
            )
            for field in profileForm.changed_data:
                setattr(profileForm, field, profileForm.cleaned_data.get(field))
            # El ultimo elemento registrado
            lastUser = User.objects.latest('id')
            newProfile = Profile(
                user=lastUser,
                tel_1=profileForm.tel_1,
                razon_social=profileForm.razon_social if hasattr(
                    profileForm, "razon_social") else "",
                rfc=profileForm.rfc if hasattr(profileForm, "rfc") else "",
                direccion_fiscal=profileForm.direccion_fiscal if hasattr(
                    profileForm, "direccion_fiscal") else "",
                ciudad=profileForm.ciudad if hasattr(
                    profileForm, "ciudad") else "",
                estado_fact=profileForm.estado_fact if hasattr(
                    profileForm, "estado_fact") else "",
                tel_2=profileForm.tel_2 if hasattr(
                    profileForm, "tel_2") else "",
                correo_fact=profileForm.correo_fact if hasattr(
                    profileForm, "correo_fact") else "",
                cfdi=profileForm.cfdi if hasattr(
                    profileForm, "cfdi") else "",
                direccion=profileForm.direccion if hasattr(
                    profileForm, "direccion") else "",
                municipio=profileForm.municipio if hasattr(
                    profileForm, "municipio") else "",
                estado=profileForm.estado if hasattr(
                    profileForm, "estado") else "",
                cp=profileForm.cp if hasattr(profileForm, "cp") else "",
                numero_ext=profileForm.numero_ext if hasattr(
                    profileForm, "numero_ext") else None,
                numero_int=profileForm.numero_int if hasattr(
                    profileForm, "numero_int") else None,
                entre_calle=profileForm.entre_calle if hasattr(
                    profileForm, "entre_calle") else "",
                entre_calle_2=profileForm.entre_calle_2 if hasattr(profileForm, "entre_calle_2") else "",)
            newProfile.save()
            messages.success(request, 'La cuenta de ' +
                             newProfile.user.username + ' ha sido creada. Ya puede iniciar sesión')
            return redirect('/inicio_sesion')
        else:
            print("Verifique los datos")
    context = {
        'user': userForm,
        'profile': profileForm,
    }
    return render(request, 'demo/register.html', context)


@login_required(login_url='login')
def user_profile(request):
    if request.method == 'POST':
        # Recuperar los datos
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        tel_1 = request.POST['tel_1']
        direccion = request.POST['direccion']
        estado = request.POST['estado']
        municipio = request.POST['municipio']
        cp = request.POST['cp']
        numero_ext = request.POST['numero_ext']
        numero_int = request.POST['numero_int']
        entre_calle = request.POST['entre_calle']
        entre_calle_2 = request.POST['entre_calle_2']
        razon_social = request.POST['razon_social']
        rfc = request.POST['rfc']
        direccion_fiscal = request.POST['direccion_fiscal']
        ciudad = request.POST['ciudad']
        estado_fact = request.POST['estado_fact']
        tel_2 = request.POST['tel_2']
        correo_fact = request.POST['correo_fact']
        cfdi = request.POST['cfdi']
        # Comprobar que los números, sean números
        try:
            numero_int = int(numero_int)
        except:
            numero_int = None
        try:
            numero_ext = int(numero_ext)
        except:
            numero_ext = None
        # Actualizarlos de acuerdo al usuario
        user = request.user
        # Model User
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        # Profile
        profile = Profile.objects.get(user=request.user)
        profile.tel_1 = tel_1
        profile.direccion = direccion
        profile.estado = estado
        profile.municipio = municipio
        profile.cp = cp
        profile.numero_ext = numero_ext
        profile.numero_int = numero_int
        profile.entre_calle = entre_calle
        profile.entre_calle_2 = entre_calle_2
        profile.razon_social = razon_social
        profile.rfc = rfc
        profile.direccion_fiscal = direccion_fiscal
        profile.ciudad = ciudad
        profile.estado_fact = estado_fact
        profile.tel_2 = tel_2
        profile.correo_fact = correo_fact
        profile.cfdi = cfdi
        user.save()
        profile.save()
    profile = Profile.objects.get(user=request.user)
    context = {'profile': profile}
    return render(request, 'demo/user_profile.html', context)


@login_required(login_url='login')
def user_history(request):
    compras = Compra.objects.filter(
        usuario=request.user, status_compra=status_choices.EN_PROCESO)
    historial = Compra.objects.filter(
        usuario=request.user, status_compra=status_choices.ENTREGADO)
    context = {'compras': compras, 'historial': historial}
    return render(request, 'demo/user_history.html', context)
