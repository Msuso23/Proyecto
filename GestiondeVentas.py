from GestiondeClientes import GestiondeClientes
from GestiondeProductos import GestiondeProductos
from GestiondePagos import  GestiondePagos
from GestiondeEnvios import GestiodeEnvios


class GestiondeVentas:
    #Primero creamos el constructor para establecer los atributos necesarios

    def __init__ (self,cliente,productos,cantidad,pago,envio,subtotal,descuentos,iva,igtf,total,fecha):
        self.cliente=cliente
        self.productos=productos
        self.cantidad=cantidad
        self.pago=pago
        self.envio=envio
        self.subtotal=subtotal
        self.descuentos=descuentos
        self.iva=iva
        self.igtf=igtf
        self.total=total
        self.fecha=fecha
        self.CompraProductos=[]
        self.ventas=[]
        self.gestiondeClientes=GestiondeClientes

    
    #Una serie de metodos para simplificar los calculos y no crear un solo metodo largo
    def calcular_descuento(self):
        if GestiondeClientes.tipo == "Juridico":
            self.descuentos=self.subtotal * 0.05
        else:
            self.descuentos= 0
 
    def calcular_iva(self):
        self.calcular_subtotal
        self.iva= self.subtotal * 0.16
    
    def calcular_igtf(self):
        if GestiondePagos.tipodepago == "Efectivo" or self.pago=="Tarjeta internacional" or self.pago=="Zelle":
            self.igtf= self.subtotal * 0.03
        else:
            self.igtf= 0


    def calcular_subtotal(self):    
        self.subtotal= sum(i[1] * i[2] for i in self.CompraProductos)


    def calcular_Total(self):
        self.calcular_descuento() 
        self.calcular_iva()
        self.calcular_igtf()    
        self.total = self.subtotal - self.descuentos + self.iva + self.igtf

    #Metodo de validacion para simplificar donde sea necesario

    def validacionCI(self,CI):
        while not CI.isdigit():
                print("Introduzca una cedula valida")
                CI=input("CI: ")
    
    #En este metodo primero llamamos a otras clases para poder acceder a atributos de ellas
    #Elaboro unos condicionales para poder buscar y utilizar los objetos deseados y mensajes de error
    #por si no se encuentra registrado


    def RegistrarVenta(self, clienteB, prodB):
        clienteB=GestiondeClientes()
        prodB=GestiondeProductos()
        print("Desea buscar el cliente mediante cedula o email?")
        decisionCI=input("CI (1) correo(2)")
        while decisionCI not in ("1" ,"2"):
            print("Introduzca una opcion valida")
            print("Desea buscar el cliente mediante cedula o email?")
            decisionCI=input("CI (1) correo(2)")
        if decisionCI=="1":
            cedulacliente=input("CI del cliente: \n")
            self.validacionCI(cedulacliente)
            cliente=clienteB.buscar_CI(cedulacliente)

        elif decisionCI=="2":
            correocliente=input("Correo del cliente:\n")
            cliente=clienteB.buscar_correo(correocliente)
        if cliente is None:
            print("El cliente no se encuentra registrado.")
            return

        #Se dan a conocer los atributos del cliente que se establecieron para evitar confusiones

        print(f"La compra es a nombre de {cliente.nombre} {cliente.apellido}")
        
        #Ahora ocurre lo mismo pero con los productos con ligeros cambios, ya que se debe decidir la cantidad
        #a comprar de cada uno 

        print("Desea agregar un producto?")
        AgregarProductos=input("Si (1) No(2)")
        while AgregarProductos =="1":
            print("Que producto va a comprar")
            producto=input("Nombre del producto:")
            prod=prodB.buscar_name(producto)
            if prod is None:
                print("No disponemos del producto")
                return
            else:
                cantidad=int(input("Cantidad a comprar:"))
                precio=prod.precio
                self.CompraProductos.append([prod, cantidad, precio])
            AgregarProductos=input("Si (1) No(2)")

        #Se accede al modulo GestiondePagos para que sea una compra consistente, es decir, que no sea cada uno
        #independiente sino que se relacionen dando un mejor funcionamiento, estableciendo mismos valores 
        #y simplificando el codigo


        self.pago=GestiondePagos(self.cliente)
        
        self.pago.RegistrarPago()
        self.pago.RegistrarFechaActual()
        self.fecha = self.pago.fecha

        #Lo mismo con el modulo GestiondeEnvios
        self.envio=GestiodeEnvios()
        self.envio.RegistrarEnvio() 


        #Se ejecutan los calculos utilizando los valores de gestiondePago conjunto a los de los productos
        
        self.calcular_Total()
        self.total+=self.envio.costoenvio

        #Se determina el costo, se muestra el total con y sin descuento, en caso de no tener sera el mismo

        print(f"Subtotal antes de descuentos: {self.subtotal}")
        print(f"El total de la compra sería: {self.total}")

        #Y para finalizar se pregunta si realmente se quiere comprar, ya que pueden ocurrir confusiones con los precios
        #anadiendo a dos listas distintas, la de pagos y la de ventas. Imprimiendo los datos generales y la factura
        #En caso de no confirmar simplmente el proceso llega hasta ahi sin anadir objetos y entregando un mensaje de cancelacion

        print("Confirma la venta?")
        confirmar = input("Si (1) No(2): ")
        while confirmar not in ("1", "2"):
            confirmar = input("Introduzca '1' para confirmar o '2' para cancelar: ")
            
        if confirmar == "1":       
            print("Compra realizada con exito")
            self.listPagos.append({
                "cliente": self.cliente,
                "productos": self.CompraProductos,  
                "total": self.total
            })
            print("Su factura")
            self.Factura()

            self.listVentas.append(self)        

        else:   
            print("Venta cancelada.")
            
        

    #Metodo para mostrar los atributos

    def Factura(self):
        print(f'''
          cliente: {self.cliente.nombre}
          productos: {self.CompraProductosproductos}
          cantidad: {self.cantidad}
          total: {self.total}
          direccion: {self.gestiondeClientes.direccion}
          fecha: {self.fecha} 
          ''')

    #Metodos de busqueda como los de GestiondeProductos (revisar esos docstrings para explicacion)

    def SearchClientesVentas(self):
        buscar= False
        nombre=input("Nombre del producto: \n")
        for x in self.listClientes:
            if x.nombre==nombre:
                buscar=True
                print("Se encuentra en la lista")
                x.Factura()
        if not buscar:
            print("El cliente no está registrado")

    def SearchFechaVentas(self):
        buscar = False
        fecha_buscar = input("Introduzca la fecha a buscar (mm/dd/aaaa, hh:mm:ss): ") 
        for venta in self.ventas:
            if venta.fecha == fecha_buscar:
                buscar = True
                print("Se ha encontrado una coincidencia")
                venta.Factura()  
        if not buscar:
            print("No se han encontrado coincidencias")

    def SearchMontoVentas(self):
        buscar=False
        MontoABuscar=input("Introduzca el monto a buscar: ")
        for i in self.listPagos:
            if i.total==MontoABuscar:
                buscar=True
                print("Existen coincidencias")
                i.Factura()
        if not buscar:
            print("No hay compras con ese monto")
