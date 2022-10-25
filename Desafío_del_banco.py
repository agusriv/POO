
class Cuenta_Bancaria:
    
    def __init__(self, DNI):
        # Atributos de instancia
        self.DNI = DNI
        # Al momento de iniciar no hay transacciones
        self.listado_de_transacciones = []

        # Metodos Propios
    def __str__(self):
        return "DNI: {}".format(self.DNI)

    def registrar_transacciones(self, tipo_de_movimiento, Monto_de_la_operacion, fecha):
        transaccion = Transaccion(tipo_de_movimiento, Monto_de_la_operacion, fecha)
        self.listado_de_transacciones.append(transaccion)

    def mostrar_transacciones(self):
        for items in self.listado_de_transacciones:
         print( items)

        # Para guardar las transacciones se tiene que ingresar el DNI de la cuenta para saber de que cuenta es la información
    
    def guardar_transacciones(self, DNI_de_la_cuenta):
        ruta_carpeta = r"C:\Users\agustin\OneDrive\Escritorio\Transacciones"
        archivo = open(ruta_carpeta + "/transacciones_de_cuentas.txt", "a")
        
        for items in self.listado_de_transacciones:
            archivo.write("DNI de la cuenta: {}".format(DNI_de_la_cuenta) + "\n" + str(items) + "\n" )
            archivo.close


class Transaccion:

    def __init__(self, tipo_de_movimiento, Monto_de_la_operacion, fecha):
        
        # Atributos de instancia
        self.tipo_de_movimiento = tipo_de_movimiento
        self.Monto_de_la_operacion = Monto_de_la_operacion
        self.fecha = fecha

    # Debe retornar SI o SI un string
    def __str__(self):
        return """Tipo de movimiento: {} 
Monto de la operacion: {} 
Fecha: {}\n""".format(self.tipo_de_movimiento,self.Monto_de_la_operacion, self.fecha)

#==============================================================================================================       

# Instanciar objetos (crear)

cuenta_bancaria = Cuenta_Bancaria("55987958")
print( cuenta_bancaria )
cuenta_bancaria.registrar_transacciones("Retiro", "USD 10.000", "16/10/2022")
cuenta_bancaria.mostrar_transacciones()
cuenta_bancaria.guardar_transacciones(55987958)
        
cuenta_bancaria2 = Cuenta_Bancaria("46283854")
print( cuenta_bancaria2 )
cuenta_bancaria2.registrar_transacciones("Deposito", "USD 1.000", "14/9/2022")
cuenta_bancaria2.mostrar_transacciones()
cuenta_bancaria2.guardar_transacciones(46283854)

cuenta_bancaria3 = Cuenta_Bancaria("234567134")
print( cuenta_bancaria2 )
cuenta_bancaria3.registrar_transacciones("Retiro", "USD 3.000", "18/7/2022")
cuenta_bancaria3.mostrar_transacciones()
cuenta_bancaria3.guardar_transacciones(234567134)



