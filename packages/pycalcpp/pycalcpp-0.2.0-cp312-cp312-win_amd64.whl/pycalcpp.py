"""Modulo de c++ a python con pybind11"""

import Operaciones
import documentos

class PyCal:
    def __init__(self,a,b):
        self.a = a
        self.b = b


    def sumar(a,b):
        """Muestra la suma de dos numeros"""
        return Operaciones.suma(a,b)

    def restar(a,b):
        """Muestra la resta de dos numeros"""
        return Operaciones.resta(a,b)

    def multiplicar(a,b):
        """Muestra la multiplicacion de dos numeros"""
        return Operaciones.multiplicacion(a,b)

    def dividir(a,b):
        """Muestra la division de dos numeros"""
        return Operaciones.division(a,b)


    def sumarx(a,b):
        """Muestra la suma de dos numeros en la consola"""
        return Operaciones.suma_console(a,b)

    def restarx(a,b):
        """Muestra la resta de dos numeros en la consola"""
        return Operaciones.resta_console(a,b)

    def multiplicarx(a,b):
        """Muestra la multiplicacion de dos numeros en la consola"""
        return Operaciones.multiplicacion_console(a,b)

    def dividirx(a,b):
        """Muestra la division de dos numeros en la consola"""
        return Operaciones.division_console(a,b)

    def docux():
        """Muestra la documentacion de la clase"""
        return documentos.enviar()


