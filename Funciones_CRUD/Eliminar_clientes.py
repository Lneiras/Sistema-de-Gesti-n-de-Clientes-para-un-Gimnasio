from OFunciones.aspectos_visuales import *
from OFunciones.Otras_funciones import *
from Funciones_CRUD.Buscar_usuario import *


def Eliminar_cliente(Lista_clientes):
    limpiar_pantalla()

    if not Lista_clientes: #Si el usuario consulta esta opción sin tener productos en el inventario se mostrara ese mensaje
        print(f"{Azul}\nNo hay usuarios registrados.{Reset}")
        return

    while True:

        User = Buscar_cliente(Lista_clientes)

        '''En esta parte nos aseguramos que si en la funsión "Buscar_clientes" el usuario escribe 'salir' y devuelve un valor None
        con el 'return' la función se cierra sin pasar a la siguiente parte de la función'''
        if User is None: 
            print(f"\n{Amarillo}Operación de actualización cancelada.{Reset}")
            return
        
        salir = ""

        while salir != 1:

            Eliminar = input(f"\n{Amarillo}Confirma si deseas eliminar este cliente (Si/No):  {Reset}").strip().lower()

            if Eliminar == "si":
                Lista_clientes.remove(User)
                print(f"{Rojo}Cliente eliminado{Reset}")
                Volviendo()
                return
            
            elif Eliminar == "no":
                print(f"\n{Amarillo}Eliminación cancelada{Reset}")
                Volviendo()
                salir = 1

            else:
                print(f"\n{Rojo}Error: opcion invalida, intenta de nuevo{Reset}")
                continue