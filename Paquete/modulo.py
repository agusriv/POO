class Persona:
    def __init__(self, Nombre, Apellido):
        
        self.Nombre = Nombre
        self.Apellido = Apellido

    def Hablar(self, nombre_persona):
        print("Hola soy {}, como estas {}?".format(self.Nombre, nombre_persona))