from re import template
from xmlrpc.client import NOT_WELLFORMED_ERROR
from django.http import HttpResponse
from datetime import datetime
from django.template import Context, Template, loader   #para generar template
import random
from home.models import Persona

def crear_persona(request, nombre, apellido, edad, fecha_nacimiento):
    
    persona = Persona(nombre=nombre, apellido=apellido, edad=edad, fecha_nacimiento=fecha_nacimiento)
    persona.save()          #GUarda la persona en la base de datos
    template = loader.get_template('crear_persona.html')    
    template_renderizado = template.render({'persona': persona})
    
    return HttpResponse('')

def ver_personas(request):
    
    #le paso a la base de datos todfos los objetos de personas
    
    persona = Persona.objects.all()
    template = loader.get_template('ver_persona.html')    
    template_renderizado = template.render({'personas': persona})
    
    return HttpResponse(template_renderizado)