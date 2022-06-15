
listaCliente=[]

class cliente:
    """
    esta clase clientes sirve para el control de las solicitudes que realizan para conseguir una carrera
    atributos:
        nombre=str
        apellido=str
        edad=str
        telefono=str 
    Metodos:
        nombre=str
        ingreso del nombre al momento de registrar un nuevo cliente
        apellido=str
        Para poder continuarcon el registro se necesita el ingreso del apellido
        edad=str
        se necesita la edad para si poder saber si elcliente es mayor de 16 años para podder usar el servicio
        telefono=str 
        Asi mismo el telefono para mantener en contacto al cliente por via whatsapp
    """
    def __init__(self, nombre, apellido,edad):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
    def datos(nombre,apellido,cedula,edad):
        #se validara la edad en caso de ser menor de edad saldra edad negada y si es mayor de 65 igualmente sera negada
        if edad>=15 and edad<=75 :
            print ("EDAD PERMITIDA")
            telefono=str(input("INGRESA TU NUMERO PARA ESTAR EN CONTACTO: "))
            listaCliente.append(telefono)  
     
        else:
            print ("==================================================================================") 
            print("EDAD NO PERMITIDA POR SER MENOR DE EDAD, VUELVA A INGRESAR")
            print ("==================================================================================")

    def sesion(usuario,passw,nombre,cedula):
        if usuario==nombre and passw==cedula:
            print("LOS DATOS INGRESADOS SON CORRECTOS")
            """
            Una vez que el usuario verifique sus datos sele pedira que ingrese su lugar de recogida, referencia del  sector
            de regida y lugar de llegada
            INGRESE EL LUGAR DE RECOGIDA: MUCHO LOTE MZ.2624
            INGRESE UNA REFERENCIA DEL SECTOR: DETRAS DE LA  FERIA DE CARROS
            INGRESE EL LUGAR DE LLEGADA: CIUDADELA LA FAE
            """
            print ("====================================================================") 
            lugarI=str(input("INGRESE EL LUGAR DE RECOGIDA: "))
            referencia=str(input("INGRESE UNA REFERENCIA DEL SECTOR: "))
            lugarFi=str(input("INGRESE EL LUGAR DE LLEGADA: "))
            print ("====================================================================") 
            cliente.mostrar(lugarI,referencia,lugarFi) 
        else:
            print("Datos mal ingresados")
    
    def mostrar(lugarI,referencia,lugarFi):
        print ("====================================================================")
        print ("             SOLICITUD FUE REALIZADA EXITOSAMENTE")
        print ("====================================================================")        
        print ("NOMBRE Y APELLIDO: ",listaCliente[1]," ",listaCliente[2]," EDAD-",listaCliente[4] )
        print ("CEDULA DE IDENTIFICACION: ",listaCliente[3],"    N-TELEFONO ",listaCliente[0])
        print ("====================================================================")
        print ("LUGAR DE PARTIDA: ",lugarI)
        print ("REFERENCIA DEL  LUGAR DE RECOGIDA: ",referencia) 
        print ("LUGAR DE LLEGADA: ",lugarFi)
        print ("====================================================================")
        print ("       AVISO: SE HARA UN DESCUENTO DEL 25% POR FERIADO")
        print ("====================================================================")

def subCliente():
        opcionCliente= int
        while opcionCliente!=3:
            opcionCliente=int(input("\n======================================= \nCOOPERATIVA °LA FAMILIA°: \n======================================= \n 1:REGISTRATE, SI ERES CLIENTE NUEVO \n 2:INICIA SESIÓN, SI YA ERES  USUARIO \n 3:VOLVER AL MENU PRINCIPAL \n======================================= \n INGRESE UNA OPCION:  "))
            if opcionCliente==1:
                print ("====================================================================")
                print ("            ERES CLIENTE NUEVO REGISTRATE Y VIAJA SEGURO ")
                print ("====================================================================") 
                """
                En la opcion 1 desplegara el regiustro primero se le pedira aL usuario que ingrese sus datos principales esto ayudara 
                a la compañia al momento de hacer una carrera, 
                """
                """
                En esta seccion se le pedira al nuevo usuario que ingrese sus datos para haci poder disponer del servicio, el usuario para 
                poder regitrarse debera ingresar su nombre, apellido, edad (si el usuario es menor de 16 años, se le permitira el registro pero
                con supervisión de los padres, asi  mismo si es mayor de 75 serasolo bajo supervision de un familiar), cedula y telefono, ejemplo
                INGRESE SUS NOMBRE: GREGORY
                INGRESE SUS APELLIDO: CHEVEZ
                INGRES SU EDAD: 20
                EDAD PERMITIDA
                INGRESA TU NUMERO DE CEDULA O PASAPORTE: 0952799708
                INGRESA TU NUMERO DE TELFONA PARA PODER ESTAR EN CONTACTO CONTIGO A LO QUELLEGEEL CHOFER: 0975781238
                """
                # Asignacion de variables a usar en nuestro codigo
                nombre=str(input("INGRESE SUS NOMBRE: "))
                apellido=str(input("INGRESE SUS APELLIDO: "))
                cedula=str(input("INGRESA TU NUMERO DE CEDULA O PASAPORTE: "))
                edad=int(input("INGRES SU EDAD: "))
                cliente.datos(nombre,apellido,cedula,edad)
                listaCliente.append(nombre)
                listaCliente.append(apellido)
                listaCliente.append(cedula)
                listaCliente.append(edad)
            elif opcionCliente == 2:
                print ("====================================================================")
                print ("          HOLA VIAJERO QUE SE SIENTE VIAJAR SEGURO DE NUEVO ")
                print ("====================================================================")
                """
                Al seleccionar la opcion 2 desplegara el inicio de seción del usuario solicitando su nombre como usuario y su numero de cedula 
                como contraseña, EJEMPLO:
                INGRESE SU USUARIO O NOMBRE REGISTRADO: GREGORY
                INGRESE SU CONTRASEÑA: 0952799708
                """
                usuario=str(input("INGRESE SU USUARIO O NOMBRE REGISTRADO: "))
                passw=str(input("INGRESE SU CONTRASEÑA: "))
                # Verificacion del usuario y la contraseña
                cliente.sesion(usuario,passw,nombre,cedula)
            elif opcionCliente == 3:
                print("REGRESANDO AL MENU PRNCIPAL.........")
            else:
                print("ERROR, OPCION INCORRECTA")