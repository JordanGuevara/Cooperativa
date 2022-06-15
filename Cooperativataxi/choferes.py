import datetime
import requests
import os
import argparse
import re
import json
from dateutil.easter import easter
from dateutil.relativedelta import relativedelta as rd, FR
from holidays.constants import JAN, MAY, JUN, AUG, OCT, NOV, DEC
from holidays.holiday_base import HolidayBase
"""
Se usan estas librerias para asi poder usar las fechas que ayudan al momento de los feriados y poder saber cuales dias aplica
descuento y cuales no
"""
from clientes import *
import random
from datetime import datetime 

"""
Se utiliza para llamar o importar el contenido de todos 
los metodos y clases por medio de from "nombre archivo.py" import "nombre de metodos"

El from "datatime" nos da acceso a la fecha y hora para poder mostrarlo o darle utilidad en nuestro codigo
"""
fecha=datetime.today().strftime('%m-%d')  
año=datetime.today().strftime('%Y')
"""
Asignacion de variables para que encapsule el "Año-Mes-Día"
"""
listaCarro=[]
listaChofer=[]
"""
Creación de listas que encapsulan los datos que se van a ingresar, como se da en el ejemplo
listaCarro=[]
listaCarro.append("Toyota")
"""

class FiestasEcuador(HolidayBase): # 
    """
    Clase para hacer mas sencillo los feriados, el cual tendra referencia las provincias las cuales son pasados por herencia.
    https://www.turismo.gob.ec/wp-content/uploads/2020/03/CALENDARIO-DE-FERIADOS.pdf
    ...
    Atributos (clase padre) 
    ---------- prov: str código de provincia según ISO3166-2 Métodos ------- 
        __init__(self, plate, date, time, online=False) : 
         Construye todos los atributos necesarios para el objeto HolidayEcuador.
        _populate(self, year): Devuelve si una fecha es festiva o no
        """     
    IMPR_PROVINCIAS = ["EC-P"]  # TODO añadir más provincias
    """
    Códigos ISO 3166-2 (estan en los metodos)), 
    llamadas provincias, con esto podremos llamar a las 24 provincias existentes en el Ecuador
    https://es.wikipedia.org/wiki/ISO_3166-2:EC
    """

    def __init__(self, **kwargs):# kwargs a diferencia del self es un argumeto para poder declarar una funcion 
        """
             Construye todos los atributos necesarios para el objeto HolidayEcuador.
        """         
        self.country = "ECU"
        self.provincia = kwargs.pop("prov", "ON") # eliminar la clave especificada y devolver el valor correspondiente
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        """
        Comprueba si una fecha es festiva o no Parámetros 
        ----------
             año : str año de una fecha Devuelve 
         ------
             Devuelve verdadero si una fecha es festiva de lo contrario flase
        """                    
        # año nuevo 
        self[datetime.date(year, JAN, 1)] = "Año Nuevo [New Year's Day]"
        
        # navidad
        self[datetime.date(year, DEC, 25)] = "Navidad [Christmas]"

        #Dia de la madre
        self[datetime.date(year, MAY, 1)]="Dia de la madre "
        
        #Dia del padre
        self[datetime.date(year, JUN, 1)]="Dia del padre"
        
        #Dia de la independecia
        self[datetime.date(year, MAY, 24)]="Dia de la independecia"
class Feriados:
    """
    Una clase para representar los feriados y que comprobar o validar de que la fecha pueda ser un feriado
    Atributos
    ----------       
    fecha: str 
        Fecha en la que el vehículo pretende transitar
        esta siguiendo el, Formato ISO 8601 AAAA-MM-DD: por ejemplo, 2020-04-22.
    en línea: booleano, opcional
        si en línea == Verdadero, se utilizará la API de días festivos abstractos
    Métodos
    -------
    __init__(self, date, online=False):
        Construye todos los atributos necesarios, que son usado en la clase feriado
    fecha (uno mismo):
        Obtiene el valor del atributo de fecha
    fecha (auto, valor):
        Establece el valor del atributo de fecha
    __find_day(yo, fecha):
        Devuelve el día a partir de la fecha: 
        por ejemplo, miércoles
    __es_vacaciones:
        Devuelve True si la fecha marcada (en formato ISO 8601 AAAA-MM-DD) es un día festivo en Ecuador,
        de lo contrario, Falso
    predecir (auto):
        Devuelve True si la fecha ingresada cae un dia feriado, de lo contrario, de vuelve Falso cuando ese dia no existe un feriado 
        
        """ 
    #Days of the week
    __days = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday"]

    def __init__(self, date, online=False):
        """
        Construye todos los atributos necesarios para el objeto PicoPlaca.
        
         Parámetros
         ----------
             fecha: calle
                 Fecha en lacual se puede hacer un descuento al momento de contratar el servicio
                 Sigue el formato ISO 8601 AAAA-MM-DD: por ejemplo, 2020-04-22.
             en línea: booleano, opcional
                 si en línea == Verdadero, se usará la API de días festivos abstractos (el valor predeterminado es Falso)               
        """                
        
        self.date = date
        self.online = online

    @property
    def date(self):
        """
            Obtiene el valor del atributo de fecha
        """
        return self._date


    @date.setter
    def date(self, value):
        """
        Establece el valor del atributo de fecha
         Parámetros
         ----------
         valor: cadena
        
         aumenta
         ------
         ValorError
             Si la cadena de valor no tiene el formato AAAA-MM-DD (por ejemplo, 2021-04-02)
        """
        try:
            if len(value) != 10:
                raise ValueError
            datetime.datetime.strptime(value, "%Y-%m-%d")
        except ValueError:
            raise ValueError(
                'LA FECHA DE CUMPPLIR EL SIGUIENTE FORMATO ARA PODER SER VAIDA: AAAA-MM-DD (POR EJEMPLO: 2021-04-02)') from None
        self._date = value

    def __is_holiday(self, date, online):
        """
        Comprueba si la fecha (en formato ISO 8601 AAAA-MM-DD) es un día festivo en Ecuador
         si en línea == Verdadero, utilizará una API REST, 
         de lo contrario, generará los días festivos del año examinado
        
         Parámetros
         ----------
         fecha: calle
             Está siguiendo el formato ISO 8601 AAAA-MM-DD: 
             por ejemplo, 2020-04-22
         en línea: booleano, opcional
             si en línea == Verdadero, se utilizará la API de días festivos abstractos
         Devoluciones
         -------
         Devuelve True si la fecha marcada (en formato ISO 8601 AAAA-MM-DD) es un día festivo en Ecuador,
          de lo contrario, Falso        
          """            
        y, m, d = date.split('-') # separar con -

        if online:
            # API de vacaciones abstractapi, versión gratuita: 1000 solicitudes por mes
             # 1 solicitud por segundo
             # recuperar la clave API de la variable de entorno
            key = os.environ.get('HOLIDAYS_API_KEY')
            response = requests.get(
                "https://holidays.abstractapi.com/v1/?api_key={}&country=EC&year={}&month={}&day={}".format(key, y, m, d))
            if (response.status_code == 401):
                # Esto significa que falta una clave API
                raise requests.HTTPError(
                    'Falta la clave API. Guarde su clave en la variable de entorno HOLIDAYS API_KEY')
            if response.content == b'[]':  # si no hay vacaciones, obtenemos una matriz vacía
                return False
            # Arreglar el Jueves Santo incorrectamente denotado como feriado
            if json.loads(response.text[1:-1])['name'] == 'Jueves Santo':
                return False
            return True
        else:
            ecu_holidays = FiestasEcuador(prov='EC-P')
            return date in ecu_holidays


    def predict(self):
        """
        Comprueba si la fecha ingresada es un dia festivo o no:
        Devoluciones
         -------
         Devoluciones
         Devuelve True si la fecha 
         ingresada cae un dia feriado, 
         de lo contrario, 
         de vuelve Falso cuando ese dia no existe un feriado 
        """
        # Comprobar si la fecha es un día festivo
        if self.__is_holiday(self.date, self.online):
            return True
        return False


class registroChofer:
    """
    la  clase VehiculosChoferes contiene las variables para el registro de los vehiculos y choferes  nuevos
    Se usaran los atributos:
    Atributos:
        matricula=str
        marca=str
        cedulap=str
        nombres=str
        apellidos=str
        edad=str
    Metodos
        matricula=str
        perimte el ingreso de la matricula del vehiculo que se va registrar,(Ejemplo: MATRICULA DEL VEHICULO: GRM-1504)
        marca=str
        se ingresa el modelo del vehiculo, (Ejemplo:CHEVROLET "CAMARO 2022")
        cedulap=str
        se ingresa la cedula del dueño del vehiculo, (Ejemplo:0952799708)
        nombres=str
        Aqui se debe ingresar el nombre del chofe el cual trabajar en el vehiculo, (Ejemplo: Khris)
        apellidos=str
        Asi mismo se ingresa el apellido del chofe el cual trabajar en el vehiculo, (Ejemplo: Khris)
        tipoLic=str
        Se debe ingresar el tipo de licencia, (Ejemplo: tipo c) 
    """
    #Constructor de objeto de nuestros choferes
    def __init__(self, matricula, marca, cedulap, nombres, apellidos, tipoLic):
        self.matricula=matricula
        self.marca=marca
        self.cedulap=cedulap
        self.nombres=nombres
        self.apellidos=apellidos
        self.tipoLic=tipoLic
    
    def entrar(usuario,admin,contrasena,contra):
        condicion2=True
        if usuario==admin and contrasena==contra:
            print("LOS DATOS INGRESADOS SON CORRECTOS")
            print ("====================================================================")
            print ("             REGISTRO DE VEHICULOS Y CHOFERES ")
            print ("====================================================================")
            VCHnuevos=int
            """  
            El while nos ayudara a poder verificar que se ha llegado a la cantidad prevista de taxistas a registrar
            """ 
            while condicion2==True: 
                VCHnuevos=int(input("INGRESE LA CANIDAD DE TAXISTAS QUE VAN HACER REGISTRADOS: "))  
                """    
                El for servira para hacer el bucle del ingreso de los nuevos taxis, si ingresa 2 se repitira 2 veces permitiendo el ingreso de 
                taxistas de la cantidad indicada
                """  
                if VCHnuevos<=3:
                    for i in range(VCHnuevos):
                        """
                        En estas lineas de codigo el administrador de la cooperativa podra ingresar los nuevos vehiculos y choferes que trabajaran en
                        la cooperativa esto seria  un ejemplo de como se registra:
                        INGRESE LA MATRICULA DEL VEHICULO: GRM-1504
                        INGRESE EL MODELO Y LA MARCA DEL VEHICULO: CHEVROLET "CAMARO 2022"
                        INGRESE EL NUMERO DE CEDULA DEL USUARIO: 0952799708
                        INGRESE LOS NOMBRES DEL CONDUCTOR: KARLOS GREGORY
                        INGRSE LOS APELLIDOS DEL CONDUCTOR: CHEVEZ BAZAN
                        INGRESE EL TIPO DE LICENCIA DEL CONDUCTOR: TIPO C
                        """
                        print ("====================================================================")
                        print ("             REGISTRO DE VEHICULOS  ")
                        print ("====================================================================")
                        matricula=str(input("INGRESE LA MATRICULA DEL VEHICULO: "))
                        marca=str(input("INGRESE EL MODELO Y LA MARCA DEL VEHICULO: "))
                        cedulap=int(input("INGRESE EL NUMERO DE CEDULA DEL USUARIO: "))
                        
                    for i in range(VCHnuevos):
                        print ("====================================================================")
                        print ("             REGISTRO DE CHOFERES  ")
                        print ("====================================================================")
                        nombres=str(input("INGRESE LOS NOMBRES DEL CONDUCTOR: "))
                        apellidos=str(input("INGRSE LOS APELLIDOS DEL CONDUCTOR: "))
                        tipoLic=str(input("INGRESE EL TIPO DE LICENCIA DEL CONDUCTOR: "))
                        print ("====================================================================")
                        condicion2=False
                    listaCarro.append(matricula)
                    listaCarro.append(marca)
                    listaCarro.append(cedulap)
                    listaChofer.append(nombres)
                    listaChofer.append(apellidos)
                    listaChofer.append(tipoLic)
                else: 
                            print(" INGRESE CORRECTAMENTE EL NUMERO DE TAXISTAS A REGISTRAR")
            c=registroChofer.registrochofer()
            print(c)
        else:
            print("LOS DATOS INGRESADOS SON INCORRECTOS, VUELVA A INGRESAR:")
            print ("====================================================================")

        
    def solicitudes():
        """
        En la opcion dos el administrador podra observar que personas han solicitado un pedido, adicional a esto se le reflejara
        que dias tendra un descuento, esto dias son los dias festivos, entos dias los clientes tendra un descuento el cual sera
        de 25% para cualquier carrera
        """
        print ("=============================================================================")
        print ("             SOLICITUD FUE REALIZADA EXITOSAMENTE")
        print ("=============================================================================")        
        print ("NOMBRE Y APELLIDO: ",listaCliente[1]," ",listaCliente[2]," EDAD-",listaCliente[4] )
        print ("CEDULA DE IDENTIFICACION: ",listaCliente[3],"    N-TELEFONO ",listaCliente[0])
        print ("=============================================================================") 
        print ("FECHA EN LA QUE REALIZADO LA SOLICITUD DEL SERVICIO ",str(año),"-"+str(fecha))
        # Asignacion de variable con un numero random decimal con su limitante
        pago=random.uniform(3,7)
        """
        Estos datos sobre los feriados suceden durante el año en unos internacionales y otros nacionales en el Ecuador fueron encontrados 
        por este medio https://www.eluniverso.com/noticias/ecuador/los-dias-que-son-feriados-en-ecuador-para-este-2022
        -nota/#:~:text=En%20Ecuador%20anualmente%20se%20cuenta,obligatorio%20para%20todos%20los%20ecuatorianos. gracias a esta información existente 
        pudimos armar nuestro codigo de forma veridica.
        """
       
    def registrochofer():
        """
        Metodoque imrime los datos ingresados por el administrador, de los nuevos vehiculos con cheferes que ingresaran a trabaar
        """
        print("====================================================================")
        print ("|    NOMBRES    |    APELLIDOS   |   TIPO DE CCONDUCCION   |")
        for i in range(len(listaChofer)):
            print(listaChofer[i], end="   ")
        print("\n====================================================================")
        print ("| MATRICULA | MARCA | CEDULA |")
        for i in range(len(listaCarro)):
            print(listaCarro[i], end="   ")

def menuAdmin():
    subAdmin=int
    while subAdmin!=3:
        subAdmin=int(input("\n======================================= \nCOOPERATIVA °LA FAMILIA°: \n======================================= \n 1:REGISTRO DE TAXIS, SOLO ADMINISTRADORES \n 2:SOLICITUDES HECHAS \n 3:VOLVER AL MENU PRINCIPAL \n======================================= \n INGRESE UNA OPCION:  "))
        if subAdmin==1:
            """
            En la opcion 1 desplegara el inicio de seción el cual solo tendra el administrador al momento de registrar algun nuevo vehiculo o chofer
            esto hara que el programa se seguro al momento de que el cliente o alguna persona mala intente ingresar.
            Para poder ingresar esta seccion, el administrador solo tiene acceso a ella la cual el usuario y la contraseña son:
            admin=("jordan")
            contra=("losrapidos")
            """
            admin=("jordan")
            contra=("losrapidos")
            print ("====================================================================")
            usuario=str(input("INGRESE EL EL USUARIO: "))
            contrasena=str(input("INGRESE LA CONTRASEÑA: "))
            registroChofer.entrar(usuario,admin,contrasena,contra)
        elif subAdmin==2:
            registroChofer.solicitudes()
        elif subAdmin==3:
            print("REGRESANDO AL MENU PRNCIPAL.........")
        else: 
            print("ERROR, OPCION INCORRECTA")





