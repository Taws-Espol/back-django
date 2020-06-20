from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import (
    HttpResponse,
    JsonResponse
)
import json

from .models import *

# Create your views here.
@csrf_exempt
def persona(request):
	if request.method ==  "GET":
		datos = Persona.objects.all()
		lista_persona = []
		for i in datos:
			p = {}
			p["nombre"] = i.nombre
			p["cedula"] = i.cedula
			p["email"] = i.email
			lista_persona.append(p)
		personas = {"personas":lista_persona}

	elif request.method ==  "POST":

		print(request.body)
		datos = json.loads(request.body.decode('utf8'))
		print(datos)
		try:
			verificacion_usuario = Persona.objects.get(cedula = datos.get("cedula"))
			datos_retornar = {"mensaje": "Cedula ya ingresada"}
			print(datos_retornar)
			return HttpResponse(json.dumps(datos_retornar, ensure_ascii=False).encode("utf-8")\
			, content_type='application/json')
		except Exception as e:
			print(e)

		persona = Persona()
		persona.nombre = datos.get("nombre")
		persona.apellido = datos.get("apellidos")
		persona.edad = datos.get("edad")
		persona.email = datos.get("email")
		persona.cedula = datos.get("cedula")
		persona.save()
		personas = {"mensaje":"Registro exitoso"}

	return HttpResponse(json.dumps(personas, ensure_ascii=False).encode("utf-8")\
        , content_type='application/json')

def eliminar_persona(request, cedula_persona):
	try:
		persona = Persona.objects.filter(cedula = cedula_persona)
		print(persona)
		if len(persona) == 0:
			return HttpResponse(json.dumps({"mensaje":"No existe persona registrada con esta cedula"}, ensure_ascii=False).encode("utf-8")\
        , content_type='application/json')
		persona.delete()
		return HttpResponse(json.dumps({"mensaje":"Eliminado exitosamente"}, ensure_ascii=False).encode("utf-8")\
        , content_type='application/json')
	except Exception as e:
		return HttpResponse(json.dumps({"mensaje":"Error al eliminar"}, ensure_ascii=False).encode("utf-8")\
        , content_type='application/json')
