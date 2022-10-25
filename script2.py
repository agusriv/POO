import sys

# Validar cantidad de argumentos
if len(sys.argv) == 3:
    
    nota1 = sys.argv[1]
    nota2 = sys.argv[2]

    if not nota1.isdigit() or not nota2.isdigit():
        print("Cuidado! Debes pasarme solo numeros")
        sys.exit()

    nota1 = int(nota1)
    nota2 = int(nota2)

    if (0 <= nota1 <= 10) and (0 <= nota2 <= 10):
        
        if nota1 >= 7 and nota2 >= 7:
            print("Promocionado")
        
        elif nota1 >= 4 and nota2 >= 4:
            print("Aprobado, debe rendir final")
        
        elif (nota1 < 4 and nota2 >= 4) or (nota1 >=4 and nota2 < 4):
            if nota1 < 4:
                print("Desaprobado, debe recuperar el primer parcial")
            else:
                print("Desaprobado, debe recuperar el segundo parcial")
        
        else:
            print("Desaprobo ambos parciales, debe recursar.")
    else:
        print("Error: Notas fuera de rango")
        sys.exit()
else:
    print("Uso: python aprobado.py <nota1> <nota2>")
