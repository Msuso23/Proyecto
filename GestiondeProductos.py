

class GestiondeProductos:
  #Primero creamos el constructor para establecer los atributos necesarios
  def __init__(self,name,description,price,category,inventario):
    self.name=name
    self.description=description
    self.price=price
    self.category=category
    self.inventario=inventario

  "El orden de los metodos puede cambiar ya que no seran ejecutados en este modulo"


  #Creamos el metodo showProducts el cual sera util a la hora de ver los atributos de un objeto nuevo
  #o de alguno existente dependiendo de en que momento sea llamado, en mi caso lo usare en todo momento para
  #que este claro con que se esta trabajando

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
  
