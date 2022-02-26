from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Empezamos con Django")

def despedida(request):
    return HttpResponse("Acabamos con la clase")   