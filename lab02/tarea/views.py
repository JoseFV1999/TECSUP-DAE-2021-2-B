from django.shortcuts import render
import math

def formularioOperaciones(request):
    context = {
        'titulo' : 'Formulario',
    }
    return render(request, 'tarea/operaciones.html', context)

def calcularOperacion(request):
    valor1 = int(request.POST['valor1'])
    valor2 = int(request.POST['valor2'])
    operacion = request.POST['operacion']
    print (operacion)
    if (operacion=="suma"):
        respuesta = valor1 + valor2
        signo = "+"
    if (operacion=="resta"):
        respuesta = valor1 - valor2
        signo = "-"
    if (operacion=="multiplicacion"):
        respuesta = valor1 * valor2
        signo = "*"
    context = {
        'titulo' : "Respuesta",
        'valor1' : request.POST['valor1'],
        'valor2' : request.POST['valor2'],
        'operacion' : signo,
        'respuesta' : respuesta
    }
    return render(request, 'tarea/resultadoOperaciones.html', context)

def formularioCilindro(request):
    context = {
        'titulo' : 'CALCULO DEL VOLUMEN DE UN CILINDRO',
    }
    return render(request, 'tarea/cilindro.html', context)

def calcularCilindro(request):
    diametro = float(request.POST['diametro'])
    altura = float(request.POST['altura'])
    volumen = math.pi*((diametro/2)**2)*altura
    context = {
        'titulo' : "Respuesta",
        'volumen' : volumen,
    }
    return render(request, 'tarea/resultadoCilindro.html', context)