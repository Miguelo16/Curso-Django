from curses.ascii import HT
import datetime
from django.http import HttpResponse

def saludo(request):

    formato="""
        <html>
            <body>
                <h1>Empezamos con Django</h1>
            </body>
        </html>"""
    return HttpResponse(formato)

def despedida(request):
    return HttpResponse("Acabamos con la clase")

def damefecha(request):
    fecha_actual=datetime.datetime.now()

    formato="""
        <html>
        <body>
        <h2>
        Fecha y hora actual %s
        </h2>
        </body>
    </html>""" % fecha_actual

    return HttpResponse(formato)

def calculaEdad(request, edad, agno):
    #edad_actual=30
    periodo=agno-2022
    edad_futura=edad+periodo
    formato="""<html>
        <body>
        <h2>
        En el año %s tendras %s años
        </h2>
        </body>
    </html>""" %(agno, edad_futura)

    return HttpResponse(formato)