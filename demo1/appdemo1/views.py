from django.shortcuts import render
from .models import alumno


def datos(request):
    
    todo = alumno.objects.all()
    #persona = alumno.objects.values_list('name', flat=True)
    return render(request, 'mostrar.html',{'todo':todo})

# Create your views here.
