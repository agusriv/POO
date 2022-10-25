class Pasajero:

    def __init__(self, nombre_apellido, documento):
        
        self.nombre_apellido = nombre_apellido
        self.documento = documento

    def __str__(self):
        return f"{self.nombre_apellido} - Doc: {self.documento}"


class Vuelo:

    def __init__(self, cant_asientos, origen, destino):
        self.cant_asientos = cant_asientos
        self.origen = origen
        self.destino = destino
        
        # Cuando iniciamos el vuelo, no hay pasajeros
        self.listado_pasajeros = []


    def __str__(self):
        return f"{self.origen}-{self.destino} --> {len(self.listado_pasajeros)}/{self.cant_asientos}"


    def agregar_pasajero(self, nombre_apellido, documento):
        pasajero = Pasajero(nombre_apellido, documento)

        if len(self.listado_pasajeros) < self.cant_asientos:
            self.listado_pasajeros.append(pasajero)

    def imprimir_listado_pasajeros(self):
        for pasajero in self.listado_pasajeros:
            print(pasajero)

# ==================================================

vuelo = Vuelo(5, "Buenos Aires", "Mendoza")
print("Estado del vuelo: ", vuelo)


vuelo.agregar_pasajero("Leonel Gareis", "123")
vuelo.agregar_pasajero("Emiliano Scarfo", "234")
vuelo.agregar_pasajero("Cristian Garcia", "345")
vuelo.agregar_pasajero("nidia Alvarez", "456")
vuelo.agregar_pasajero("Juan Carlos Nieto", "567")
vuelo.agregar_pasajero("Damian Lucci", "789")


print("Estado del vuelo: ", vuelo)
vuelo.imprimir_listado_pasajeros()