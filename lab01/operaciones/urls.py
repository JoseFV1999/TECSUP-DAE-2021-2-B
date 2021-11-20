from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sumar/<int:valor1>/<int:valor2>', views.suma, name='suma'),
    path('restar/<int:valor1>/<int:valor2>', views.resta, name='resta'),
    path('multiplicar/<int:valor1>/<int:valor2>', views.multiplicacion, name='multiplicacion'),
    path('dividir/<int:valor1>/<int:valor2>', views.division, name='division'),
]