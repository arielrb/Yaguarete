from django.db import models
from django.contrib.auth.models import User
class Categoria(models.Model):
	descripcion = models.CharField(max_length = 150, null= True)

	def __str__(self):
	    return self.title



class Producto(models.Model):
	title = models.CharField(max_length=60, null= True)
	precio = models.FloatField(null= True)
	fecha = models.DateField(null= True)
	descripcion = models.CharField(max_length = 150, null= True)
	imagen = models.ImageField(null=True, blank=True)
	categoria = models.ForeignKey(Categoria,on_delete= models.SET_NULL, null= True)

	def __str__(self):
		return f"{self.title} de valor {self.precio}$"



class Carrito(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	productos = models.ForeignKey(Producto,on_delete=models.SET_NULL, null = True)
	#total = models.float_field(productos.precio.sum)
	def __str__(self):
		return f'El usuario {self.user} tiene en su carro '