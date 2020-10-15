if 5 > 2:
    print("5 es mayor que 3")
distancia = 8
tiempo = 2
velocidad = 0

velocidad = distancia / tiempo
print("la aceleraciones igual a: " + str(velocidad))

distancia, tiempo = 6, 3
velocidad = distancia / tiempo
print(velocidad)

name = "joseMaria"
print("hola soy " + name)

mensaje = "hola soy"
name2 = "joseMaria"
separador = " "
print(mensaje + separador + name2)

"""
text type : str
numeric types : int, float, complex
sequence types : list, tuple, range
mapping type : dict
set types : set, frozenset
bollean type : bool
binary types : bytes, bytearray, memoryview
"""

a = 5
print(a)
print(type(a))
a = "hello"
print(a)
print(type(a))
a = 2.0
print(a)
print(type(a))
a = 2j
print(a)
print(type(a))
a = ["juan", "luis"]
print(a)
print(type(a))

a = str(5)
print(a)
print(type(a))

import random

numero = random.randrange(1, 10)
print("El numero al azar es: " + str(numero))

import random

numero = random.randrange(2, 10, 2)
print("El numero al azar, par, es: " + str(numero))
