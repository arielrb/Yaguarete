from django.urls import path, include
from . import views

app_name = "Usuarios"
urlpatterns = [
    path('', views.registrarse, name="registrarse"),
]