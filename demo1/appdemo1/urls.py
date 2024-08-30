from django.urls import path, include
from .views import datos

urlpatterns = [
    path('persona/', datos, name='datos' )
]

