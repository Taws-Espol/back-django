from django.db import models

# Create your models here.

class Persona(models.Model):
	"""docstring for Persona"""
	nombre = models.CharField(max_length=100,default="SIN NOMBRE")
	apellidos = models.CharField(max_length=100,default="SIN NOMBRE")
	edad = models.IntegerField(default = 18)
	email = models.EmailField(default = " ")
	cedula = models.CharField(max_length = 10, default = "0912345678")
	def save(self,*args, **kwargs):
		super(Persona,self).save(*args, **kwargs)

	
	

class Producto(models.Model):
	"""docstring for Persona"""
	nombre = models.CharField(max_length=10, default = "SIN NOMBRE")
	precio = models.DecimalField(max_digits=10,decimal_places = 2,default=0.0)
	def save(self,*args, **kwargs):
		super(Producto,self).save(*args, **kwargs)

