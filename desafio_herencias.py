class Mamifero:

    def __init__(self, cant_mamas, esperanza_de_vida):
        self.cant_mamas = cant_mamas
        self.esperanza_de_vida = esperanza_de_vida

    def mamar(self):
        pass

    def nacer(self):
        pass

class AnimalMarino:

    def __init__(self, tiene_branqueas, especie) -> None:
        self.tiene_branqueas = tiene_branqueas
        self.especie = especie

    def nadar(self):
        pass


class Cetaceo(Mamifero, AnimalMarino):

    def __init__(self, cant_mamas, esperanza_de_vida, tiene_branqueas, especie, notas, vive_en, peso):
        
        self.notas = notas
        self.vive_en = vive_en
        self.peso = peso

        Mamifero.__init__(self, cant_mamas, esperanza_de_vida)
        AnimalMarino.__init__(self, tiene_branqueas, especie)

cetaceo  = Cetaceo(2, 12, True, "delfin", "Ninguna", "Mar del Plata", 200)

cetaceo.nacer()
cetaceo.nadar()

print( cetaceo.cant_mamas )
