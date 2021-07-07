from django.shortcuts import render
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
    return render(request,"Front/carrito.html",{
        "carrito": Carrito.objects.all()
    })
