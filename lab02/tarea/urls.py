from django.urls import path

from . import views

app_name = 'tarea'

urlpatterns = [
    path('operacion', views.formularioOperaciones, name='formularioOperaciones'),
    path('operacion/resultado', views.calcularOperacion, name='operaciones'),
    path('cilindro', views.formularioCilindro, name='formularioCilindro'),
    path('cilindro/resultado', views.calcularCilindro, name='cilindro'),
]