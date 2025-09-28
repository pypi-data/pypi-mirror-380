#ifndef MS_WIN64
#define MS_WIN64
#endif
#include <iostream>
#include <stdexcept>
#include <pybind11/pybind11.h>

namespace py = pybind11;
using namespace std;

//---------------- Operaciones matemáticas -----------------
double suma(double a, double b) {
    return a + b;
}

double resta(double a, double b) {
    return a - b;
}

double multiplicacion(double a, double b) {
    return a * b;
}

double division(double a, double b) {
    if (b == 0.0) throw std::runtime_error("No se puede dividir entre cero");
    return a / b;
}

//---------------- Operaciones con salida en consola --------
double suma_console(double a, double b) {
    double resultado = a + b;
    cout << resultado << endl;
    return resultado;
}

double resta_console(double a, double b) {
    double resultado = a - b;
    cout << resultado << endl;
    return resultado;
}

double multiplicacion_console(double a, double b) {
    double resultado = a * b;
    cout << resultado << endl;
    return resultado;
}

double division_console(double a, double b) {
    if (b == 0.0) throw std::runtime_error("No se puede dividir entre cero");
    double resultado = a / b;
    cout << resultado << endl;
    return resultado;
}

//---------------- Binding con Python -----------------------
PYBIND11_MODULE(Operaciones, m) {
    m.doc() = "Operaciones en C++ con double (soporta enteros y flotantes grandes)";

    m.def("suma", &suma, py::arg("a"), py::arg("b"), "Suma dos números (double)");
    m.def("resta", &resta, py::arg("a"), py::arg("b"), "Resta dos números (double)");
    m.def("multiplicacion", &multiplicacion, py::arg("a"), py::arg("b"), "Multiplica dos números (double)");
    m.def("division", &division, py::arg("a"), py::arg("b"), "Divide dos números (double)");

    m.def("suma_console", &suma_console, py::arg("a"), py::arg("b"), "Suma y muestra en consola");
    m.def("resta_console", &resta_console, py::arg("a"), py::arg("b"), "Resta y muestra en consola");
    m.def("multiplicacion_console", &multiplicacion_console, py::arg("a"), py::arg("b"), "Multiplica y muestra en consola");
    m.def("division_console", &division_console, py::arg("a"), py::arg("b"), "Divide y muestra en consola");
}

