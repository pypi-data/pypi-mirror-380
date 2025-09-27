"""Modulo de c++ a python """

import Operaciones

app = Operaciones

def sumar(a,b):
    """Muestra la suma de dos numeros"""
    return app.suma(a,b)

def restar(a,b):
    """Muestra la resta de dos numeros"""
    return app.resta(a,b)

def multiplicar(a,b):
    """Muestra la multiplicacion de dos numeros"""
    return app.multiplicacion(a,b)

def dividir(a,b):
    """Muestra la division de dos numeros"""
    return app.division(a,b)


def sumarx(a,b):
    """Muestra la suma de dos numeros en la consola"""
    return app.suma_console(a,b)

def restarx(a,b):
    """Muestra la resta de dos numeros en la consola"""
    return app.resta_console(a,b)

def multiplicarx(a,b):
    """Muestra la multiplicacion de dos numeros en la consola"""
    return app.multiplicacion_console(a,b)

def dividirx(a,b):
    """Muestra la division de dos numeros en la consola"""
    return app.division_console(a,b)