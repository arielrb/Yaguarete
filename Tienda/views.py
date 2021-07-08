from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from .models import *
# Create your views here.
@login_required()
def index(request):
    return render(request,"Front/index.html", {
        "lista_productos": Producto.objects.all().order_by('-fecha')[:10],
    })
def carrito(request):
    usuario_activo = User.objects.all().exclude(last_login = None)[0].id
    return render(request,"Front/carrito.html",{
        "carrito": Carrito.objects.all().filter(user= usuario_activo )
    })
def pantalla_principal(request):
    producto_clikeado = Producto.objects.all().filter()
    return render(request, "Front/pantalla_principal.html",{
        "agregar_carrito": None,

    })
