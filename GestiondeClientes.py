class GestiondeClientes():
  #Primero creamos el constructor para establecer los atributos necesarios

    def __init__(self, nombre,apellido,tipo,ci,correo,direccion,telefono):
        self.nombre=nombre
        self.apellido=apellido
        self.tipo=tipo
        self.ci=ci
        self.correo=correo
        self.direccion=direccion
        self.telefono=telefono

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
