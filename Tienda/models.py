from django.db import models

class Categoria(models.Model):
	title = models.CharField(max_length = 20, null= True)
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
		return f"{self.title} de valor {self.precio}"



class Carrito(models.Model):
#	user = models.OneToOneField(user, on_delete=models.CASCADE)
#    products = models.foreign_key(Producto,on_delete=models.SET_NULL, null = True)
	def __str__(self):
		return self.name