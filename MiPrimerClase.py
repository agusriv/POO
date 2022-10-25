
class persona:
    #Atributos de clase
    Nacionalidad = "Uruguay"
    idioma = "Español"

    def __init__(self, nombre, edad, CI):

        # Atributos de instancia

        self.nombre = nombre
        self.edad = edad
        self.CI = CI

    # Metodos Propios
    def saludar(self, destinatario):
        print("hola que tal, soy {} ¿Cómo estas {}?".format(self.nombre, destinatario))
    def informacion(self):
        print("Nombre: {}, Edad: {}, CI: {}".format(self.nombre, self.edad, self.CI))
    def __str__(self):
        # Debe retornar SI o SI un string
        return f"Persona: Nombre: {self.nombre}; Edad: {self.edad} "


# Instanciar objetos
persona1 = persona("Agustin", 16, 55987958)
persona2 = persona("Belen", 18, 5567849)

persona2.saludar("alejandro")
persona1.informacion()
print(persona1)
print(persona2)







        

