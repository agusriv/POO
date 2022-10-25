
# Definicion de la clase
class Perro:
    
    # Atributos de clase
    nacionalidad = "Argentina"
    numero_de_patas = 4

    # Constructor de clase
    def __init__(self, nombre, raza, edad=1):
        
        # Atributos de instancia
        # Con esto decoramos el objeto
        self.nombre = nombre
        self.edad = edad
        self.raza = raza

    # Metodos propios
    def ladrar(self):
        print("guau"*5+"!")

    def avanzar(self, cant_pasos):
        # Soy XXXXX y he avanzado YY pasos.
        print(f"Soy {self.nombre} y he avanzado {cant_pasos} pasos")

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Raza: {self.raza}")


# Instanciar un objeto (crear)
perrito = Perro("Roco", "Labrador")
perrito2 = Perro("Theo", "Caniche", 3)


perrito.avanzar(3)
perrito2.avanzar(50)

perrito.raza = "Pastor Aleman"

perrito.mostrar_info()


