from django.urls import path, include
from .views import datos

urlpatterns = [
    path('', datos, name='datos'),
    path('persona/', datos, name='datos' )
]

