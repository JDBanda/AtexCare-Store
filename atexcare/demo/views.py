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


def index(request):
    context = {}
    return render(request, 'demo/index.html', context)


def products(request):
    # Filtrar los productos
    lista = ProductFilter(request.GET, queryset=Product.objects.all())
    context = {
        "productos": lista,
    }
    return render(request, 'demo/products.html', context)


def product(request, pk):
    instance = Product.objects.get(id=pk)
    # Obtener de many to many
    a = Feature.objects.filter(product=pk)
    context = {'producto': instance,
               'caracteristicas': a}
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
                    'mensaje': 'Debe ingresar o darse de alta para guardar elementos en el carrito'
                }
            })
        # Intenta insertar los datos
        try:
            usuario = User.objects.get(username=usuario)
            # Aqui faltaría agregar un status para decir que el carrito esta activo y aun no se ha pagado
            objCarrito = Carrito(
                producto=producto, cantidad=cantidad, monto=monto, usuario=usuario)
            objCarrito.save()
            return JsonResponse({
                'content': {
                    'mensaje': '¡Añadido al carrito!',
                }
            })
        except:
            context = {
                'mensaje': 'Ocurrio un error',
            }
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
                    'mensaje': 'Actualizado'
                }
            })
        except:
            return JsonResponse({
                'content': {
                    'mensaje': 'Error, vuelve a intentar'
                }
            })
    objCar = Carrito.objects.filter(usuario=request.user)
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
                    'mensaje': 'Elemento ' + nombre + ' eliminado'
                }
            })
        except:
            # Mandar mensaje
            return JsonResponse({
                'content': {
                    'mensaje': 'Ocurrió un problema al eliminar, vuelva a intentar'
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
                    profileForm, "razon_social") else None,
                rfc=profileForm.rfc if hasattr(profileForm, "rfc") else None,
                direccion_fiscal=profileForm.direccion_fiscal if hasattr(
                    profileForm, "direccion_fiscal") else None,
                ciudad=profileForm.ciudad if hasattr(
                    profileForm, "ciudad") else None,
                estado_fact=profileForm.estado_fact if hasattr(
                    profileForm, "estado_fact") else None,
                tel_2=profileForm.tel_2 if hasattr(
                    profileForm, "tel_2") else None,
                correo_fact=profileForm.correo_fact if hasattr(
                    profileForm, "correo_fact") else None,
                cfdi=profileForm.cfdi if hasattr(
                    profileForm, "cfdi") else None,
                direccion=profileForm.direccion if hasattr(
                    profileForm, "direccion") else None,
                municipio=profileForm.municipio if hasattr(
                    profileForm, "municipio") else None,
                estado=profileForm.estado if hasattr(
                    profileForm, "estado") else None,
                cp=profileForm.cp if hasattr(profileForm, "cp") else None,
                numero_ext=profileForm.numero_ext if hasattr(
                    profileForm, "numero_ext") else None,
                numero_int=profileForm.numero_int if hasattr(
                    profileForm, "numero_int") else None,
                entre_calle=profileForm.entre_calle if hasattr(
                    profileForm, "entre_calle") else None,
                entre_calle_2=profileForm.entre_calle_2 if hasattr(profileForm, "entre_calle_2") else None,)
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
    profile = Profile.objects.get(user=request.user)
    context = {'profile': profile}
    return render(request, 'demo/user_profile.html', context)


@login_required(login_url='login')
def user_history(request):
    #profile = Profile.objects.get(user=request.user)
    context = {}
    return render(request, 'demo/user_history.html', context)
