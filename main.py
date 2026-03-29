# Sistema de Gestión de Clientes para un Gimnasio con Persistencia de Datos

from OFunciones.aspectos_visuales import *
from OFunciones.Otras_funciones import *
from Funciones_CRUD.Crear_cliente import *
from Funciones_CRUD.Listar_clientes import *
from Funciones_CRUD.Buscar_usuario import *
from Funciones_CRUD.Actualizar_clientes import *
from Funciones_CRUD.Eliminar_clientes import *
from OFunciones.Data import *

#Lista_clientes

def main():

    Salir = ""

    while Salir != "si": #con este while salir evitamos usar el break para finalizar 
        limpiar_pantalla()
        print(f"\n{Verde}Bienvenido a SmartGym{Reset}\n")
        opcion = menu()

        if opcion == "1": #Esta opción nos lleva a ejecutar la función de agregar producto
            Cliente = Crear_cliente(Lista_clientes)
            Lista_clientes.append(Cliente) #Con esta función se agrega el producto a lista_inventario

        elif opcion == "2": #esta opción lista todos los usuarios registrados
            Listar_clientes(Lista_clientes)
        
        elif opcion == "3": #Esta función nos ayuda a buscar por nombre o Id de cliente   
            Buscar_cliente(Lista_clientes)
            Volviendo()

        elif opcion == "4": #Esta función nos ayuda a actualziar el tipo de plan o el estado del mismo en un cliente          
            Actualizar_cliente(Lista_clientes)

        elif opcion == "5":
            Eliminar_cliente(Lista_clientes)

        elif opcion == "6": #salimos del programa
            Salir = input(f"\n{Amarillo}Deseas salir del programa?(Si/No):  {Reset}").strip().lower()
            if Salir == "si":
                salir()
            else:
                Regresando()

        elif opcion == "7":
            guardar_datos_csv(Clientes_csv, Lista_clientes)
            print("archivo guardado con exito")
            Volviendo()
            
        else:
            print(f"{Rojo}\nError: Opción invalida, intente de nuevo{Reset}")

main()