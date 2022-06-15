"""
el from choferes import menuAdmin sirven para importar las variables o funciones que se encuentran dentro de otro
archivo, el * nos permite importar todas todos los metodos en el archivo
"""
from choferes import menuAdmin
from clientes import *

"""
Para poder solventar el problema que presente la instutucion con el registro de sus nuevos vehiculos y choferes esto
ayudara a la cooperativa a poder llevar un registro de los vehiculos y choferes nuevos que trabajan en la cooperativa. 
A su vez poder registrar a clientes nuevos y llevar un control de lo clientes que solicitan el sevicio.
"""
def menu():
    """
    El def menu es un metodo el cual posee el meenu principal de todo el programa, el menu principal se veria  asi:
    =============================== 
    COOPERATIVA "LA FAMILIA"
    =============================== 
    1:CLIENTES
    2:AGENCIA
    3:SALIR 
    =============================== 
    INGRESE UNA OPCION:
    
    Atributos
    ------------------------------
    se usa un menu con opciones multiples disponibles para que deseee el usuario  ingresar
    """
    opc= int
    while opc!=3:
        opc=int(input("\n=============================== \nCOOPERATIVA °LA FAMILIA°: \n=============================== \n 1:CLIENTES \n 2:AGENCIA \n 3:SALIR \n=============================== \n INGRESE UNA OPCION:  "))
        if opc==1:
            """
            La opcion uno nos lleva al archivo clientes el cual nos permitira el registro de nuevos clientes y 
            que el cliente pueda solicitar el servicio una ves creada su cuenta
            """
            subCliente()
        elif opc==2:
            """
            La opcion dos nos lleva al archivo choferes pero en esta seccion solo tiene permitido el ingreso los 
            administradores, ya que aqui esta el registro de nuevos vehiculos con sus respectivos choferes, adicional
            a esto se podra observar las solicitudes hechas
            """
            menuAdmin()
        elif opc==3:
            """
            Esta nos permite salir del program o darle fin a la ejecucion
            """
            print("GRACIAS POR SU VISITA")
        else:
            print("LA OPCION INGRESA ES INCORRECTA VUELVA A INGRESAR:")
        
       


            
