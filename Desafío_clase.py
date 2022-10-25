class Atleta :

    def __init__(self, Nombre, Apellido, Altura, Peso, Telefono):

        self.Nombre = Nombre
        self.Apellido = Apellido
        self.__Altura = Altura
        self.__Peso = Peso
        self.Telefono = Telefono

        # Agregar IMC

        self.imc = self.__calcular_imc()

    def __calcular_imc(self):
        valor_imc = self.__Peso / (self.__Altura **2)

        if valor_imc < 18.5:
            return "Peso inferior"
        elif 18.5 <= valor_imc < 25:
            return "Normal" 
        elif 25 <= valor_imc < 30:
            return "Sobrepeso"
        elif 30 <= valor_imc < 35:
            return "Obesidad"
        else:
            return "Obesidad Extrema"

    # Métodos GET y SET para atrivutos privados 

    def set_peso(self, nuevo_peso):
        self.__Peso = nuevo_peso
        self.imc = self.__calcular_imc()
    
    def get_peso(self):
        return self.__Peso

    def set_altura(self, nueva_altura):
        self.__Altura = nueva_altura
        self.imc = self.__calcular_imc()

    def get_altura(self):
        return self.__Altura

    def __str__(self):
        return """Nombre: {} 
Apellido: {} 
IMC: {}\n""".format(self.Nombre, self.Apellido, self.imc)

atleta = Atleta("Agustin", "Rivera", 1.85, 76, "099562125")

print(atleta)

atleta.set_peso(98)
print(atleta)

atleta.set_altura(1.75)
print(atleta)




        
