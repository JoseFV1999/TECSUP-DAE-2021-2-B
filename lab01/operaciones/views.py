from django.http import HttpResponse

def index(request):
    return HttpResponse("Escoja una operacion con /suma, /resta, /multiplicacion, /division")

def suma(request, valor1, valor2):
    return HttpResponse("La suma de %s + %s = %s." %(valor1, valor2, valor1+valor2))

def resta(request, valor1, valor2):
    return HttpResponse("La resta de %s - %s = %s." %(valor1, valor2, valor1-valor2))

def multiplicacion(request, valor1, valor2):
    return HttpResponse("La multiplicacion de %s * %s = %s." %(valor1, valor2, valor1*valor2))

def division(request, valor1, valor2):
    return HttpResponse("La division de %s / %s = %s." %(valor1, valor2, valor1/valor2))