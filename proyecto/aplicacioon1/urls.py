from . import views
from django.conf.urls import  url
from django.urls import path



urlpatterns = [
    url(r'^persona', views.persona, name="persona"),
    url(r'^eliminarPersona/(?P<cedula_persona>\d+)', views.eliminar_persona, name="controlador"),

]
