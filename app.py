from GestiondeProductos import GestiondeProductos
from GestiondeClientes import GestiondeClientes
from GestiondeEnvios import GestiodeEnvios
from GestiondePagos import GestiondePagos
from GestiondeVentas import GestiondeVentas
from API import data
import datetime
import random

class App:
    #Primero creamos el constructor para establecer los atributos necesarios
    #Este caso es un poco peculiar ya que son listas
    def __init__(self,listClientes=[],listPagos=[],listProductos=[],listEnvios=[],listVentas=[ ]):
        self.listClientes=listClientes
        self.listPagos=listPagos
        self.listProductos=listProductos
        self.listEnvios=listEnvios
        self.listVentas=listVentas
        #Esto se hace con el fin de intentar extraer los datos del txt y si esta vacio da error
        #se ejecuta el except y llama al metodo que descarga los datos del api
        self.DescargaProductos()

    
    #Estos metodos de Descargar buscan transformar la informacion almacenada en la lista a objetos,
    #abren el archivo y buscan entre las separaciones creadas por la coma para agregar cada uno de 
    #ellos como objeto a la lista, ya que usa un ciclo for
    def DescargaProductos(self):
        try:
            with open ("productos.txt") as f:
                for line in f:
                    name, description, price, category, inventory = line.split(',')  
                    producto = self(name, description, price, category, inventory) 
                    self.listProductos.append(producto)
        except FileNotFoundError:
            self.GuardarProductosApi

    def DescargarResto(self):
            with open ("clientes.txt") as f:
                for line in f:
                    nombre,apellido,tipo,ci,correo,direccion,telefono = line.split(',')
                    cliente= self(nombre,apellido,tipo,ci,correo,direccion,telefono)
                    self.listClientes.append(cliente)
        

            with open ("pagos.txt") as f:
                for line in f:
                    clientpago,monto,moneda,tipodepago,fecha = line.split(',')
                    pago= GestiondePagos(clientpago,monto,moneda,tipodepago,fecha)
                    self.listPagos.append(pago)

            with open ("envios.txt") as f:
                for line in f:
                    cliente,order,servicio,delivery,costoenvio,fecha = line.split(',')
                    envio= GestiodeEnvios(cliente,order,servicio,delivery,costoenvio,fecha)
                    self.listEnvios.append(envio)

            with open ("ventas.txt") as f:
                for line in f:
                    cliente,productos,cantidad,pago,envio,subtotal,descuentos,iva,igtf,total,fecha = line.split(',')
                    venta= GestiondeVentas(cliente,productos,cantidad,pago,envio,subtotal,descuentos,iva,igtf,total,fecha)
                    self.listVentas.append(venta)

    #Este metodo hace lo contrario a los anteriores 
    #guarda los objetos de la lista de una forma que posteriormente puedan ser usados como en los metodos 
    #anteriores

    def CargarDatos(self):
        with open("productos.txt", "w") as f:
            for product in self.listProductos:
                f.write(str(product) + "\n")
        with open("clientes.txt", "w") as f:
            for cliente in self.listClientes:
                f.write(str(cliente) + "\n")
        with open("pagos.txt", "w") as f:
            for pago in self.listPagos:
                f.append(str(pago) + "\n")
        with open("envios.txt", "w") as f:
            for envio in self.listEnvios:
                f.append(str(envio) + "\n")
        with open("vetnas.txt", "w") as f:
            for venta in self.listPagos:
                f.append(str(venta) + "\n")

    #Este metodo simplemente es para acortar la ejecucion del siguiente
    def Guardar(self):
        self.CargarDatos()
        
    def GuardarProductosApi(self):
        for product in data:
            name = product["name"]
            description = product["description"]
            price = product["price"]
            category = product["category"]
            inventory = product["inventory"]
            
            product.GuardarProducto(name, description, price, category, inventory)
    

    #Creamos el metodo DescargaApi para vaciar todos los valores del API en la lista de productos y convertirlos en objetos
    #como ocurre con los primeros metodos, utilizando una busqueda sencilla, posteriormente se crea un nuevo metodo
    #para facilitar el llamado

    
    
    #Creamos un menu sencillo basando sus opciones en numeros para mayor facilidad al validar
    #Cada numero accede a uno de los modulos y sus metodos, teniendo cada uno distintos metodos y propositos
    #Utilizando el while True para correrlo como un ciclo y poder validar

    def menu(self):
        print("Bienvenido a la tienda de gestion de productos naturales")
        while True:
            print("\nMENU") 
            print("\nA que seccion desea acceder?")
            print("1. Gestion de productos")
            print("2. Gestion de clientes")
            print("3. Gestion de pagos")
            print("4. Gestion de ventas")
            print("5. Gestion de envios")
            print("6. Estadisticas")
            print("7. Salir")
            #El condicional de utiliza para validar que sea una de las opciones disponibles, ya que
            #el while se encargara de correrlo en caso de que no sea asi
            #Se utiliza el break para romper el ciclo una vez realizada la gestion deseada
            #Asi funciona en cada uno de los tipos de gestion excepto el ultimo el cual se ecarga solo de dar fin

            seleccion=input("Ingrese el numero de la seccion; \n")
            if seleccion=="1":
                print("\nHa ingresado a la gestion de Productos")    
                print("Que accion desea realizar?")
                print("1. Ver productos")
                print("2. Agregar productos")
                print("3. Buscar producto (Permite modificar las caracteristicas del mismo y eliminar productos)")
                print("4. Salir")
                
                
                while True:
                    seleccionProductos=input("Ingrese el numero de la accion que desea realizar:\n")
                    if seleccionProductos in ["1", "2", "3","4"]:
                        if seleccionProductos=="1":
                            self.MostrarProductos(self.listProductos)
                        elif seleccionProductos=="2":
                            self.GuardarProducto(self.listProductos)
                        elif seleccionProductos=="3":
                            print("""Desea realizar la busqueda por
                            1. Nombre
                            2. Precio
                            3. Categoria
                            4. Disponibilidad
                            """)
                            while True:
                                SeleccionBusquedaP=input("Ingrese el numero de la opcion:\n ")
                                if SeleccionBusquedaP in ["1", "2", "3","4"]:
                                    if SeleccionBusquedaP =="1":
                                        nombre=input("Nombre del producto: \n")
                                        self.buscar_name(self,nombre,self.listProductos)
                                    elif SeleccionBusquedaP=="2":
                                        precio=input("Precio: \n")
                                        self.buscar_price(precio,self.listProductos)
                                    elif SeleccionBusquedaP=="3":
                                        cat=input("Categoria a la que pertenece: \n")
                                        self.buscar_category(cat,self.listProductos)
                                    elif SeleccionBusquedaP=="4":
                                        dispo=input("Numero de unidades disponibles en el inventario: \n")
                                        self.buscar_inv(dispo,self.listProductos)
                                    break
                                else:
                                    print("Por favor ingrese (1),(2),(3) o (4)")
                        
                        else:
                            break


            elif seleccion=="2":
                print("\nHa ingresado a la gestion de Clientes")    
                print("Que accion desea realizar?")
                print("1. Ver clientes")
                print("2. Agregar clientes")
                print("3. Buscar clientes (Permite modificar sus caracteristicas y eliminarlos)")
                print("4. Salir")

                while True:
                    selecionClientes=input("Ingrese el numero de la accion que desea realizar:\n")
                    if selecionClientes in ["1","2","3","4"]:
                        if selecionClientes=="1":
                            self.showCliente(self.listClientes)
                        elif selecionClientes=="2":
                            self.GuardarCliente(self.listClientes)
                        elif selecionClientes=="3":
                            print("""Desea realizar la busqueda por
                            1. Correo
                            2. CI
                            """)
                            while True:
                                seleccionBusquedaC=input("Ingrese el numero de la opcion:\n")
                                if seleccionBusquedaC=="1" or seleccionBusquedaC=="2":
                                    if seleccionBusquedaC=="1":
                                        inputmail=input("Correo electronico: ")
                                        self.validacionMail(inputmail)
                                        self.buscar_correo(inputmail,self.listClientes)
                                    elif seleccionBusquedaC=="2":
                                        inputCI=input("CI: ")
                                        self.validacionCI(inputCI)
                                        self.buscar_ci(inputCI,self.listClientes)
                                    break
                                
                                else:
                                    print("Por favor ingrese una opcion valida")

                        else:
                            break
                        
            elif seleccion=="3":
                print("\nHa ingresado a la gestion de pagos")
                print("Que accion desea realizar?")
                print("1. Registrar pagos")
                print("2. Buscar pagos")
                print("3. Salir")

                while True:
                    seleccionPagos=input("Ingrese el numero de la accion que desea realizar:\n")
                    if seleccionPagos in ["1","2","3"]:
                        if seleccionPagos=="1":
                            self.RegistrarPago()
                        elif seleccionPagos=="2":
                            print("""Desea realizar la busqueda por
                                1. Cliente
                                2. Fecha
                                3. Tipo de pago
                                4. Moneda de pago
                                """)
                            while True:
                                seleccionBusquedaPagos=input("Ingrese el numero de la accion que desea realizar:\n")
                                if seleccionBusquedaPagos in ["1","2","3","4"]:
                                    if seleccionBusquedaPagos=="1":
                                        nombre=input("Nombre del cliente: \n")
                                        self.SearchClientePagos(self.listPagos,nombre)
                                    elif seleccionBusquedaPagos=="2":
                                        #Se utiliza el try except para validar el formato al tratarse de uno complicado
                                        fecha=input("mes/dia/anio, hora:minuto:segundo")
                                        fecha_formato = "%m/%d/%Y, %H:%M:%S"
                                        try:
                                            fecha.strptime(fecha,fecha_formato)
                                            self.SearchFechaPagos(self.listPagos,fecha)
                                        except ValueError:
                                            print("Formato invalido, ingrese el indicado")
                                    elif seleccionBusquedaPagos=="3":
                                        tipos_de_pago_validos = ["Tarjeta", "Pago Movil", "Tarjeta internacional", "Zelle", "Efectivo"]
                                        tipodepagoinput = input("Tipo de pago? ")

                                        while not tipodepagoinput in tipos_de_pago_validos:
                                            print("Las opciones validas son:  \n (Tarjeta)  \n (Pago Movil)  \n (Tarjeta internacional)  \n(Zelle)  \n (Efectivo)")
                                            print("Deben ser escritas igual a la opcion para obtener resultados")
                                            tipodepagoinput = input("Tipo de pago? ")
                                        self.SearchTipoPagos(self.listPagos,tipodepagoinput)
                                    elif seleccionBusquedaPagos=="4":
                                        monedadepagoinput=input("Ingrese la moneda utilizada, las opciones son: \n Dolar \n Bs")
                                        while not (monedadepagoinput=="Dolar" or monedadepagoinput=="Bs"):
                                            print("Por favor ingrese una opcion valida")
                                            monedadepagoinput=input("Ingrese la moneda utilizada, las opciones son: \n Dolar \n Bs")
                                        self.SearchMonedaPagos(self.listPagos,monedadepagoinput)
                                    break
                        else:
                            break
                                
            elif seleccion=="4":
                print("\nHa ingresado a la gestion de ventas")
                print("Que accion desea realizar?")
                print("1. Registrar venta")
                print("2. Generar facturas")
                print("3. Buscar utilizando los filtros")
                print("4. Salir")
                while True:
                    selecionVentas=input("Ingrese el numero de la accion que desea realizar:\n")
                    if selecionVentas in ["1","2","3","4"]:
                        if selecionVentas=="1":
                            self.RegistrarVenta()
                        elif selecionVentas=="2":
                            self.Factura()
                        elif selecionVentas=="3":
                            print("""Desea realizar la busqueda por
                                1. Cliente
                                2. Fecha
                                3. Monto
                                """)
                            while True:
                                seleccionBusquedaVentas=input("Ingrese el numero de la accion que desea realizar:\n")
                                if seleccionBusquedaVentas in ["1","2","3"]:
                                    if seleccionBusquedaVentas=="1":
                                        InputClienteVentas=input("Nombre del cliente: ")
                                        self.SearchClientesVentas(self.listVentas,InputClienteVentas)
                                    elif seleccionBusquedaVentas=="2":
                                        #Se utiliza el try except para validar el formato al tratarse de uno complicado
                                        #Igual que antes
                                        InputFechaVentas=("mes/dia/anio, hora:minuto:segundo")
                                        fecha_formato = "%m/%d/%Y, %H:%M:%S"
                                        try:
                                            InputFechaVentas.strptime(InputFechaVentas,fecha_formato)
                                            self.SearchFechaPagos(self.listPagos,InputFechaVentas)
                                        except ValueError:
                                            print("Formato invalido, ingrese el indicado")
                                    elif seleccionBusquedaVentas=="3":
                                        InputMontoVentas=input("Introduzca el monto: ")
                                        while not InputMontoVentas.isdigit():
                                            print("Introduzca un numero")
                                            InputMontoVentas=input("Introduzca el monto: ")
                                        self.SearchMontoVentas(self.listVentas,InputMontoVentas)
                                    break
                        else:
                            break
            

            elif seleccion=="5":
                print("\nHa ingresado a la gestion de envios")
                print("Que accion desea realizar?")
                print("1. Registrar envio")
                print("2. Buscar envios")
                print("3. Salir")

                while True:
                    seleccionEnvios=input("Ingrese el numero de la accion que desea realizar:\n")
                    if seleccionEnvios in ["1","2","3"]:
                        if seleccionEnvios=="1":
                            self.RegistrarEnvio()
                        elif seleccionEnvios=="2":
                            print("Que accion desea realizar?")
                            print("""Desea realizar la busqueda por
                                1. Cliente
                                2. Fecha
                                """)
                            while True:
                                seleccionBusquedaEnvios=input("Ingrese el numero de la accion que desea realizar:\n")
                                if seleccionBusquedaEnvios in ["1","2","3"]:
                                    if seleccionBusquedaEnvios=="1":
                                        InputClienteEnvios=input("Nombre del cliente: ")
                                        GestiondeVentas.SearchClientesVentas(self.listVentas,InputClienteEnvios)
                                    elif seleccionBusquedaEnvios=="2":
                                        InputFechaEnvios=("mes/dia/anio, hora:minuto:segundo")
                                        fecha_formato = "%m/%d/%Y, %H:%M:%S"
                                        try:
                                            InputFechaVentas.strptime(InputFechaEnvios,fecha_formato)
                                            self.SearchFechaPagos(self.listPagos,InputFechaEnvios)
                                        except ValueError:
                                            print("Formato invalido, ingrese el indicado")
                                    else:
                                        break
                        else:
                            break
            elif seleccion=="6":
                print("\nHa ingresado a las estadisticas")


            elif seleccion=="7":
                self.Guardar()
                print("Gracias por acceder al programa")
                break

    def showProducts(self):
      print(f'''
          name: {self.name}
          description: {self.description}
          price: {self.price}
          category: {self.category}
          quantity: {self.inventario}
          ''')
      

  #Creo el metodo para modificar los atributos de un producto en caso de ser necesario, este accede a los 
  #ya existentes. No es util sin los nuevos datos, los cuales seran ingresados mas adelante
    def ModificarProducto(self, desc, price, category, quantity):
            self.description = desc
            self.price = price
            self.category = category
            self.inventario = quantity

    #El metodo GuardarProducto probablemente sea el mas importante, ya que se encarga de generar nuevos productos
    #por lo tanto sera el mas utilizado. Se basa en una serie de inputs que coincidan con los atributos cada una 
    #con su validacion y al final se convierte en objeto y es anadido a la lista de los mismos

    def GuardarProducto(self):
                name=input("Name: ")
                desc=input("Description: ")
                while True:
                    try:
                        price=int(input("Price: "))
                        if price>= 0:
                            break
                        else:
                            print("INTRODUCZCA UNA NUMERO VALIDO")
                    except ValueError:
                        print("INTRODUZCA UN NUMERO")

                category=input("Category: ")
                while True:
                    try:
                        quan=int(input("Quantity: "))
                        if quan>= 0:
                            break
                        else:
                            print("INTRODUCZCA UNA NUMERO VALIDO")
                    except ValueError:
                        print("INTRODUZCA UN NUMERO")

                obj=GestiondeProductos(name,desc,price,category,quan)
                self.listProductos.append(obj)
                obj.showProducts()
                print('\n Producto registrado!\n')
            

    #Todos los metodos de buscar tienen la misma base, realizando pequenios cambios, empieza con un booleano que
    #determina si se esta buscando o no, para posteriormente iterar sobre la lista de productos y buscar coincidencias
    #entre atributos de la lista y los introducidos por el usuario. El input lo inclui en el modulo de app dentro del menu
    #(el input que realizara la comparacion)
    #Estos metodos acceden a otros para ser de mayor utilidad y no quedarse en una simple busqueda, como el de
    #modificar, el de guardar y el de borrar
    
            
    def buscar_inv(self,inventario,lista):
            buscar= False
            for x in lista:
                if x.inventario==inventario:
                    buscar=True
                    print("Se encuentra en la lista")
                    x.showProducts()

            if not buscar:
                print("El producto no está en la lista, desea agregarlo?")
                respuesta=input("Si (1) o No(2)")
                while not respuesta=="1" or respuesta=="2":
                    respuesta=input("***ERRORR INTRODUZCA UNA OPCION VALIDA*** \n Si (1) o No(2)")
                    if respuesta == "1":
                        self.GuardarProducto()
                    elif respuesta=="2":
                        pass


    def buscar_category(self,category):
            buscar= False
            for x in self.listProductos:
                if x.category==category:
                    buscar= True
                    print("Se encuentra en la lista")
                    x.showProducts()
                    
            if not buscar:
                print("El producto no está en la lista, desea agregarlo?")
                respuesta=input("Si (1) o No(2)")
                while not respuesta=="1" or respuesta=="2":
                    respuesta=input("***ERRORR INTRODUZCA UNA OPCION VALIDA*** \n Si (1) o No(2)")
                    if respuesta == "1":
                     self.GuardarProducto()
                    elif respuesta=="2":
                        pass

    def buscar_price(self,price):
            buscar= False
            for x in self.listProductos:
                if x.price==price:
                    buscar=True
                    print("Se encuentra en la lista")
                    x.showProducts()
                    Decision=input("Desea modificar el producto? Si (1) No(2) ")
                    while not Decision=="1" or Decision=="2":
                        print("Introduzca una opcion valida")
                        Decision=input("Desea modificar el producto? Si (1) No(2) ")
                    if Decision=="1":
                        desc=input("Description: ")
                        while True:
                            try:
                                pric=int(input("Price: "))
                                if pric>= 0:
                                    break
                                else:
                                    print("INTRODUCZCA UNA NUMERO VALIDO")
                            except ValueError:
                                print("INTRODUZCA UN NUMERO")
                                
                        category=input("Category: ")
                        while True:
                            try:
                                quan=int(input("Price: "))
                                if quan>= 0:
                                    break
                                else:
                                    print("INTRODUCZCA UNA NUMERO VALIDO")
                            except ValueError:
                                print("INTRODUZCA UN NUMERO")
                        x.ModificarProducto(desc,pric,category,quan)

            if not buscar:
                print("El producto no está en la lista, desea agregarlo?")
                respuesta=input("Si (1) o No(2)")
                while not respuesta=="1" or respuesta=="2":
                    respuesta=input("***ERRORR INTRODUZCA UNA OPCION VALIDA*** \n Si (1) o No(2)")
                if respuesta == "1":
                    self.GuardarProducto()
                elif respuesta=="2":
                    pass
                
        
    def buscar_name(self,nam,lista):
            buscar=False
            for x in lista:
                if x.name==nam:
                    buscar=True
                    print("Se encuentra en la lista")
                    x.showProducts()
                    Decision=input("Desea modificar el producto? Si (1) No(2) ")
                    while not Decision=="1" or Decision=="2":
                        print("Introduzca una opcion valida")
                        Decision=input("Desea modificar el producto? Si (1) No(2) ")
                    if Decision=="1":
                        desc=input("Description: ")
                        while True:
                            try:
                                price=int(input("Price: "))
                                if price>= 0:
                                    break
                                else:
                                    print("INTRODUCZCA UNA NUMERO VALIDO")
                            except ValueError:
                                print("INTRODUZCA UN NUMERO")
                                
                        category=input("Category: ")
                        while True:
                            try:
                                quan=int(input("Price: "))
                                if quan>= 0:
                                    break
                                else:
                                    print("INTRODUCZCA UNA NUMERO VALIDO")
                            except ValueError:
                                print("INTRODUZCA UN NUMERO")
                        x.ModificarProducto(desc,price,category,quan)
                    elif Decision=="2":
                        print("Desea borrar el producto?")
                        DecisionBorrar=input("Si (1) No (2)")
                        while not DecisionBorrar=="1" or DecisionBorrar=="2":
                            print("Introduzca una opcion valida")
                            DecisionBorrar=input("Si (1) No (2)")
                        if DecisionBorrar=="1":
                            self.BorrarProductoName(nam,self.listProductos)
                        elif DecisionBorrar=="2":
                            pass
                    
            if not buscar:
                print("El producto no está en la lista, desea agregarlo?")
                respuesta=input("Si (1) o No(2)")
                while not respuesta=="1" or respuesta=="2":
                    respuesta=input("***ERRORR INTRODUZCA UNA OPCION VALIDA*** \n Si (1) o No(2)")
                    if respuesta == "1":
                        self.GuardarProducto()
                    elif respuesta=="2":
                        pass
        

    #El metodo mostrarproductos itera la lista de productos completa y hace un print de cada uno ayudandose de
    #ShowProducts

    def MostrarProductos(self):
            if len(self.listProductos) == 0:
                print("No hay productos registrados.")
            else:
                print("Los productos registrados son:")
                for producto in self.listProductos:
                    producto.showProducts()

    #BorrarProducto, su nombre es bastante descriptivo. Funciona en conjunto los metodos de buscar, de otra forma
    #no sera de utilidad. Al igual que los anteriores itera la lista buscando coincidencia la cual existe, puesto
    #que viene dentro del metodo de busqueda donde coincide y elimina este elemento de la lista

    def BorrarProductoName(self,nam):
            for i in self.listProductos:
                if i.name==nam:
                    self.listProductos.remove(i)
                    print(f"{nam} ha sido eliminado.")

    #Para terminar utilizamos el API, genera un objeto por cada producto que se encuentra en ella
    
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
        prodB=self()
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

        #Se accede al modulo self para que sea una compra consistente, es decir, que no sea cada uno
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

    #Metodos de busqueda como los de self (revisar esos docstrings para explicacion)

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
        for venta in self.listVentas:
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
            self.GuardarCliente()
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
    #(Explicacion mas detallada en self)

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


#Metodo para mostrar los atributos del objeto

    def showCliente(self):
        print(f'''
            nombre: {self.nombre}
            tipo: {self.tipo}
            CI/RIF: {self.ci}
            correo: {self.correo}
            direccion: {self.direccion}
            telefono: {self.telefono}
            ''')
        
    #Metodo dependiente para modificar atributos, solo funciona para cambiarlos por valores establecidos
    #previamente, por ellos se incluye dentro de metodos mas grandes

    def ModificarCliente(self,nombre,apellido,tipo,ci,correo,direccion,telefono):
        self.nombre=nombre
        self.apellido=apellido
        self.tipo=tipo
        self.ci=ci
        self.correo=correo
        self.direccion=direccion
        self.telefono=telefono
        
    #Metodos de validacion para aligerar la carga en los metodos principales, usando ciclos

    def validacionCI(self,CI):
        while not CI.isdigit():
                print("Introduzca una cedula valida")
                CI=input("CI: ")
    
    def validacionMail(self,mail):
        while not ("@" in mail and ".com" in mail):
                print("Introduzca un correo valido")
                mail=input("Correo electronico: ")

    def validacionTip(self,tipo):
        while not tipo=="1" or tipo=="2":
                tipo=input("***ERRORR INTRODUZCA UNA OPCION VALIDA*** \n Natural (1) o Juridico(2)")
        if tipo=="2":
            self.tipo="Juridico"
        elif tipo=="1":
            self.tipo="Natural"

    def validacionTlf(self,telefono):
        while not (telefono.isdigit() and len(telefono)>=10):
                print("Introduzca un numero de telefono valido")
                telefono=input("Numero de telefono: ")

    #Metodo principal, para agregar clientes nuevo como objetos y anadirlos a la lista de clientes
    #Se ayuda de todas las validaciones hechas anteriormente para que los inputs
    
    def GuardarCliente(self):
        print("El cliente no se encuentra en la lista, desea agregarlo?")
        respuesta=input("Si (1) o No(2)")
        while not respuesta=="1" or respuesta=="2":
            respuesta=input("***ERRORR INTRODUZCA UNA OPCION VALIDA*** \n Si (1) o No(2)")
        if respuesta == "1":
            name=input("Nombre: ")
            lname=input("Apellido: ")
            tip=input("Natural (1) o Jurídico(2): ")
            if tip=="2":
                self.tipo="Juridico"
            elif tip=="1":
                self.tipo="Natural"
            self.validacionTip(tip)
            CI=input("CI: ")
            self.validacionCI(CI)
            mail=input("Correo electronico: ")
            self.validacionMail(mail)
            direccion=input("Introduzca su direccion: ")
            tlf=input("Numero de telefono: ")
            self.validacionTlf(tlf)

            #Se agregan los atributos a la clase, generando un nuevo objeto
            #se anade a la lista y posteriormente demuestra los atributos de este nuevo objeto
            #junto con un mensaje de confirmacion

            newcliente=GestiondeClientes(name,lname,tip,CI,mail,direccion,tlf)
            self.listClientes.append(newcliente)
            newcliente.showCliente()
            print('\n Cliente registrado!\n')

        #En caso de no querer registrar a un nuevo cliente, simplemente se salta y no se realiza nada
        elif respuesta=="2":
            pass


    #Metodos de busqueda, similares a los de gestiondeProductos con variaciones mas complejas


    def buscar_correo(self,correo):
        
        #Si el cliente no se encuentra en la lista se desplegan una serie de decisiones para la crear, modificar 
        #e incluso borrar estos objetos/clientes

        buscar= False
        for x in self.listClientes:
            if x.correo==correo:
                buscar=True
                print("Se encuentra en la lista")
                x.showCliente()
            Decision=input("Desea modificar la informacion del cliente? Si (1) No(2) ")
            while not Decision=="1" or Decision=="2":
                print("Introduzca una opcion valida")
                Decision=input("Desea modificar la informacion del cliente? Si (1) No(2) ")
            if Decision=="1":
                name=input("Nombre: ")
                lname=input("Apellido: ")
                tip=input("Natural (1) o Jurídico(2): ")
                while not tip=="1" or tip=="2":
                    tip=input("***ERRORR INTRODUZCA UNA OPCION VALIDA*** \n Natural (1) o Juridico(2)")
                CI=input("CI: ")
                while not CI.isdigit():
                    print("Introduzca una cedula valida")
                    CI=input("CI: ")
                mail=input("Correo electronico: ")
                while not ("@" in mail and ".com" in mail):
                    print("Introduzca un correo valido")
                    mail=input("Correo electronico: ")
                direccion=input("Introduzca su direccion: ")
                tlf=input("Numero de telefono: ")
                while not (tlf.isdigit() and len(tlf)<10):
                    print("Introduzca un numero de telefono valido")
                    tlf=input("Numero de telefono: ")
                x.ModificarCliente(name,lname,tip,CI,mail,direccion,tlf)
            
            elif Decision=="2":
                print("Desea borrar el cliente?")
                DecisionBorrar=input("Si (1) No (2)")
                while not DecisionBorrar=="1" or DecisionBorrar=="2":
                    print("Introduzca una opcion valida")
                    DecisionBorrar=input("Si (1) No (2)")
                    if DecisionBorrar=="1":
                      self.BorrarCliente(name,self.listProductos)
                    elif DecisionBorrar=="2":
                      pass

        if not buscar:    
            print("No hay coincidencias")
            self.GuardarCliente()
            Decision=input("Desea modificar la informacion del cliente? Si (1) No(2) ")
            while not Decision=="1" or Decision=="2":
                print("Introduzca una opcion valida")
                Decision=input("Desea modificar la informacion del cliente? Si (1) No(2) ")
            if Decision=="1":
                name=input("Nombre: ")
                lname=input("Apellido: ")
                tip=input("Natural (1) o Jurídico(2): ")
                while not tip=="1" or tip=="2":
                    tip=input("***ERRORR INTRODUZCA UNA OPCION VALIDA*** \n Natural (1) o Juridico(2)")
                CI=input("CI: ")
                while not CI.isdigit():
                    print("Introduzca una cedula valida")
                    CI=input("CI: ")
                mail=input("Correo electronico: ")
                while not ("@" in mail and ".com" in mail):
                    print("Introduzca un correo valido")
                    mail=input("Correo electronico: ")
                direccion=input("Introduzca su direccion: ")
                tlf=input("Numero de telefono: ")
                while not (tlf.isdigit() and len(tlf)<10):
                    print("Introduzca un numero de telefono valido")
                    tlf=input("Numero de telefono: ")
                x.ModificarCliente(name,lname,tip,CI,mail,direccion,tlf)
            
            elif Decision=="2":
                print("Desea borrar el cliente?")
                DecisionBorrar=input("Si (1) No (2)")
                while not DecisionBorrar=="1" or DecisionBorrar=="2":
                    print("Introduzca una opcion valida")
                    DecisionBorrar=input("Si (1) No (2)")
                    if DecisionBorrar=="1":
                      self.BorrarCliente(name,self.listProductos)
                    elif DecisionBorrar=="2":
                      pass

    #Metodo basico para realizar busquedas

    def buscar_ci(self,ci):
        buscar= False
        for x in self.listClientes:
            if x.ci==ci:
                buscar=True
                print("Se encuentra en la lista")
                x.showCliente()
        if not buscar:    
            print("No hay coincidencias")
            self.GuardarCliente()

    #Metodo para mostrar la totalidad de clientes registrados y sus atributos

    def MostrarClientes(self):
        if len(self.listClientes) == 0:
            print("No hay productos registrados.")
        else:
            print("Los productos registrados son:")
            for clientes in self.listCliente:
                clientes.showCliente()

    #Metodo utilizado en la anterior busqueda compleja para borrar clientes en caso de querer hacerlo
    #Es una pequenia busqueda que de ser afirmativa borra el resultado

    def BorrarCliente(self,nam,listClientes):
        for i in listClientes:
            if i.name==nam:
                listClientes.remove(i)

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



    

                                            
                                            

                        

