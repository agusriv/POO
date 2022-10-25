class Animal:

    def __init__(self, edad, especie):
        self.edad = edad
        self.especie = especie

    def hablar(self):
        pass

    def moverse(self):
        pass

    def describeme(self):
        return f"Soy un animal del tipo {type(self).__name__}"

class Perro(Animal):
    
    def __init__(self, edad, especie, nombre):
        self.nombre = nombre

        # Pasando valores a la clase padre
        super().__init__(edad, especie)


    def hablar(self):
        print("Guau!")

    def describeme(self):
        variable = super().describeme()
        return f"Soy {self.nombre}", variable
    


perrito = Perro(5, "canino", 'zeus')


print(perrito.describeme())
