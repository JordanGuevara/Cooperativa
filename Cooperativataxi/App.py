from Cooperativa import menu
from choferes import Feriados
from choferes import registroChofer
"""
Se utiliza para llamar o importar el contenido de todos 
los metodos y clases por medio de from "nombre archivo.py" import "nombre de metodos"
"""
def main():
    menu()
"""
el def main nos ayuda a poder organizar el codigo de mejor forma, esto servira para que no se vea como lineas
extensas si tener fin haciendo que el codigo se vuelva dificil de entender, como se puede apresiar el def main
llama al menu, el menu es una libreria el  cual posee el munu principal el cual tiene las opciones del programa
"""
if __name__ == '__main__':

    
    online = False
    print("=================================================================================================")
    print ('HOLA BIENVENIDO INGRESA LA FECHA DEL DIA DE HOY PARA PODER SABER SI EXISTE ALGUN FERIADO')
    fecha= input("PARA ESTO DEBES INGRESARLA DE ESTA FORMA  YYYY-MM-DD: ")
    print("=================================================================================================")
    """
    Se le pide al usuario que ingrese la fecha en acual solcita un pedido para asi poder comprobar de que si exite algun periado, 
    para esto se usa un if else, en el caso de que la fecha ingresada se correcta se le ralizara un descuento del 25%, en caso que no
    se procederacon el codigo de forma normal
    """
    pyp = Feriados(fecha, online)

    if pyp.predict():

        registroChofer.solicitudes()
        print("================================================================")
        print("HOY EN CUALQUIER PEDIDO DEL SERVICIO, TIENE UN DESCUENTO DEL 25%")
        print("================================================================")
        main()  
    else:
        print("================================================================")
        print("       HOY LASTIMOSAMENTE NO EIXTE NINGUN DESCUENTO :(")
        print("================================================================")
        main()
        