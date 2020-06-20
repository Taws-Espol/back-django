from . import views
from django.conf.urls import  url
from django.urls import path



urlpatterns = [
    url(r'^persona', views.persona, name="persona"),
    url(r'^eliminar/persona/(?P<cedula_persona>\d+)', views.eliminar_persona, name="controlador"),
    url(r'^actualizar/persona', views.actualizar_persona, name="persona"),
    url(r'^crear/producto', views.crear_prodcuto, name="producto"),
    url(r'^obtener/producto', views.obtener_productos, name="producto")
]
