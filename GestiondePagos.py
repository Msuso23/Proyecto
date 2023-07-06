from GestiondeClientes import GestiondeClientes
from datetime import datetime

#Se importa lo necesario de otros modulos
#En este caso incluso de la galeria de python



class GestiondePagos ():
  #Primero creamos el constructor para establecer los atributos necesarios

    def __init__(self,clientpago,monto,moneda,tipodepago,fecha):
        self.clientpago=clientpago
        self.monto=monto
        self.moneda=moneda
        self.tipodepago=tipodepago
        self.fecha=fecha

    #Metodo para mostrar atributos

    def showPago(self):
      print(f'''
          cliente: {self.clientpago}
          monto: {self.monto}
          moneda: {self.moneda}
          Tipo de pago: {self.tipodepago}
          fecha: {self.fecha}
          ''')
      
    #Metodo para registrar objetos, llamando a otros modulos para poder acceder a sus datos al igual 
    #que en Envios y Ventas

    def RegistrarPago(self):
        clientes = GestiondeClientes() 
        print("El cliente está registrado?")
        resp=input("Si (1) No (2)")
        while not (resp=="1" or resp=="2"):
            print("Introduzca una respuesta valida")
            resp=input("Si (1) No (2)")
        if resp=="1":
            clientCI = input("CI del cliente: \n") 
            cliente=clientes.buscar_ci(clientCI,self.listClientes)
            nombrecliente=cliente.name
            self.clientpago = nombrecliente
            
            
        elif resp=="2":
            GestiondeClientes.GuardarCliente()
            nombrecliente=GestiondeClientes.name
            self.clientpago=nombrecliente
        
        #Al igual que en otros modulos, se crean varios metodos para hace el principal mas ligero

        self.RegistrarTipodePago()
        self.RegistrarFechaActual()

    #Metodo encargado de decidir la monedavy el tipo de pago, utilizando en su mayoria condicionales
    #y validaciones para evitar errores

    def RegistrarTipodePago(self):
        print("Con que moneda va a pagar? \n Bs (1)\n Dolar(2)")
        currency=input("Seleccione una de las opciones (1) o (2)")
        while currency not in (["1","2"]):
            print("ERROR introduzca una opcion valida")
            print("Con que moneda va a pagar? \n Bs (1)\n Dolar(2)")
            currency=input("Seleccione una de las opciones (1) o (2)")
        if currency =="1":
            self.moneda="Bs"
            print("Como va a pagar? \n Tarejeta (1)\n Pago movil(2)")
            tipodepagoBs=input("(1) o (2)")
            while tipodepagoBs not in (("1","2")):
                print("ERROR introduzca una opcion valida")
                print("Como va a pagar? \n Tarjeta (1)\n Pago movil(2)")
                tipodepagoBs=input("(1) o (2)")
            if tipodepagoBs=="1":
                self.tipodepago="Tarjeta"
            else:
                self.tipodepago="Pago Movil"

        

        if currency=="2":
            self.moneda="Dolar"
            tipodepagoDol=input("Seleccione una de las opciones (1), (2) o (3)")
            while tipodepagoDol not in (["1","2","3"]):
                print("ERROR introduzca una opcion valida")
                print("Como va a pagar? \n Tarjeta internacional (1)\n Efectivo(2)\n Zelle(3)")
                tipodepagoDol=input("Seleccione una de las opciones (1), (2) o (3)")
            if tipodepagoDol=="1":
                self.tipodepago="Tarjeta internacional"
            elif tipodepagoDol=="2":
                self.tipodepago="Efectivo"
            elif tipodepagoDol=="3":
                self.tipodepago="Zelle"
            

    #Metodos para realizar busquedas como en el resto de modulos, siguiendo la misma estructura
    #(Explicacion mas detallada en GestiondeProductos)

    def SearchClientePagos(self,clientpago):
        buscar= False
        for x in self.listPagos:
            if x.clientpago==clientpago:
                buscar=True
                print("Se encuentra en la lista")
                x.showPago()
        if not buscar:
            print("No hay coincidencias")

    def SearchFechaPagos(self,fecha):
        buscar= False
        for x in self.listPagos:
            if x.fecha==fecha:
                buscar=True
                print("Se encuentra en la lista")
                x.showPago()
        if not buscar:
            print("No hay coincidencias")
    
    def SearchTipoPagos(self,tipodepago):
        buscar= False
        for x in self.listPagos:
            if x.tipodepago==tipodepago:
                buscar=True
                print("Se encuentra en la lista")
                x.showPago()
        if not buscar:
            print("No hay coincidencias")

    def SearchMonedaPagos(self,moneda):
        buscar= False
        for x in self.listPagos:
            if x.moneda==moneda:
                buscar=True
                print("Se encuentra en la lista")
                x.showPago()
        if not buscar:
            print("No hay coincidencias")

    #Metodo para tomar la fecha y hora actual, igual al de envios(Revisar gestiondeEnvios)
        
    def RegistrarFechaActual(self):
        now = datetime.now()
        self.fecha = now.strftime("%m/%d/%Y, %H:%M:%S")