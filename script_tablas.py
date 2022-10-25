"""
Desarrollar un programa que reciba como argumento
un numero, e imprima la tabla de multiplicar de ese numero
hasta el 10
"""

import sys

# Validar que nos pasen el argumento
if len(sys.argv) == 2:
    numero = int(sys.argv[1])

    for i in range(11):
        print(f"{numero}x{i} = {numero * i}")

else:
    print("Uso: python ejercicio1.py <numero>")
