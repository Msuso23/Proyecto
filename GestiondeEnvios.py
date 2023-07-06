import random
import datetime
from GestiondeClientes import GestiondeClientes 


#Se importa lo necesario de otros modulos
#En este caso incluso de la galeria de python

class GestiodeEnvios:
    #Primero creamos el constructor para establecer los atributos necesarios
    
    def __init__(self,cliente,order,servicio,delivery,costoenvio,fecha):
        self.cliente=cliente
        self.order=order
        self.servicio=servicio
        self.delivery=delivery
        self.costoenvio=costoenvio
        self.fecha=fecha

    #Creamos una funcion para elegir un numero aleatorio como numero de orden y evitar confusiones introduciendolo como inputs o de otras formas
    #Ayundandonos de la galeria de python especificamente con random

    def GenerarOrden(self):
        orden = "Orden N"
        numerorandom = random.randint(100, 999) 
        self.order = orden + str(numerorandom)
    
    #Mismo metodo de validacion que en GestiondeVentas

    def validacionCI(self,CI):
        while not CI.isdigit():
                print("Introduzca una cedula valida")
                CI=input("CI: ")
    
    #Al igual que en GestiondeVentas este modulo necesita acceder a otro para funcionar correctamente
    #por lo tanto la forma de elegir el cliente es la misma

    def RegistrarEnvio(self,clienteB):
        clienteB=GestiondeClientes()
        cedulaclienteenvios=input("CI del cliente: \n")
        self.validacionCI(cedulaclienteenvios)
        clientec=clienteB.buscar_ci(cedulaclienteenvios)
        clientec=self.cliente
        if clientec is None:
            print("El cliente no se encuentra registrado.")
            return
        
        #Se ejecutan metodos ya definidos para simplificar el procedimiento y no alargar de mas este metodo

        self.GenerarOrden()
        self.ServiciosDeEnvio()
        if self.servicio=="Delivery":
            costoenvio=1
        elif self.servicio=="MRW":
            costoenvio=3
        elif self.servicio=="Zoom":
            costoenvio=5
        elif self.servicio=="Liberty Express":
            costoenvio=2
        self.costoenvio=costoenvio

        self.RegistrarFechaActual()

        #Se incluye como objeto usando los datos recaudados y posteriormente se anade a la lista usando el append

        envio=GestiodeEnvios(clientec,self.order,self.servicio,self.delivery,costoenvio,self.fecha)
        self.listEnvios.append(envio)



            

    #Al existir dos metodos de envio se complica incluirlo en el metodo de registro por eso se crea otro metodo,
    #debido a su longitud. 
    #Este metodo es para decidir si la entrega sera via delivery o companias de envio, en caso de ser companias cuales
    #en caso de ser delivery, se ejecuta el metodo dedicado a delivery donde se deben introducir los datos del motorizado

    def ServiciosDeEnvio(self):
        print("El envio sera mediante una compania o delivery")
        SeleccionDelivery=input("Mediante una compania de envios (1) \n Mediante delivery (2)")
        while SeleccionDelivery not in (["1","2"]):
            print("ERROR EN LA SELECCION")
            print("El envio sera mediante una compania o delivery")
            SeleccionDelivery=input("Mediante una compania de envios (1) \n Mediante delivery (2)")

        if SeleccionDelivery=="1":
            print("Con cual compania de envios le gustaria trabajar")
            print("Las opciones son: 1)MRW \n 2) Liberty Express \n 3)Zoom")
            SeleccionCompania=input("Seleccione una de las opciones")
            while SeleccionCompania not in (["1","2","3"]):
                print("Con cual compania de envios le gustaria trabajar")
                print("Las opciones son: 1)MRW \n 2) Liberty Express \n 3)Zoom")
                SeleccionCompania=input("Seleccione una de las opciones")
            if SeleccionCompania=="1":
                self.servicio="MRW"
            elif SeleccionCompania=="2":
                self.servicio="Liberty Express"
            elif SeleccionCompania=="2":
                self.servicio="Zoom"
        else:
            self.servicio="Delivery"
            self.RegistrarDelivery()

        self.RegistrarFechaActual()
        

        
    def RegistrarDelivery(self):
        nombre=input("Ingrese el nombre del conductor")
        cedula=input("Ingrese el numero de cedula")
        self.validacionCI(cedula)

        print(f"""Datos del motorizado
                Nombre: {nombre}
                CI: {cedula}
                Fecha y hora de salida: {self.fecha}""")
        
    #Metodo para mostrar los atributos como se acostumbra hacer

    def showEnvio(self):
        if self.delivery is not None:
            print(f"""Datos del envio
                    Cliente: {self.cliente}
                    CI: {self.order}
                    servicio: {self.servicio}
                    Datos delivery: {self.delivery}
                    Costo del envio: {self.costoenvio}$
                    Fecha: {self.fecha}""")
        else:
            print(f"""Datos del envio
                    Cliente: {self.cliente}
                    CI: {self.order}
                    servicio: {self.servicio}
                    Costo del envio: {self.costoenvio}$
                    Fecha: {self.fecha}""")

    #Metodo para registrar la fecha y hora actual, con el fin de llevar el registro
    #para lograrlo hay que importar datetime de la galeria de python

    def RegistrarFechaActual(self):
        now = datetime.now()
        self.fecha = now.strftime("%m/%d/%Y, %H:%M:%S")

    #Metodos de buscar como los de los demas modulos (Ver gestiondeClientes)
    #de la misma manera, con los inputs en app


    def SearchFechaEnvios(self,fecha):
        buscar= False
        for x in self.listEnvios:
            if x.fecha==fecha:
                buscar=True
                print("Se encuentra en la lista")
                x.showEnvio()
        if not buscar:
            print("No hay coincidencias")


    def SearchClienteEnvios(self,cliente):
        buscar= False
        for x in self.listEnvios:
            if x.cliente==cliente:
                buscar=True
                print("Se encuentra en la lista")
                x.showEnvio()
        if not buscar:
            print("No hay coincidencias")
