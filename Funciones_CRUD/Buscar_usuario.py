from OFunciones.aspectos_visuales import *
from OFunciones.Otras_funciones import *
from OFunciones.Data import *


def busqueda_ID(clientes, ID_Buscado):
        
    for Num_id in clientes:
        if str(Num_id["ID"]) == ID_Buscado:
            return Num_id        
    return None

def busqueda_name(clientes, Name_Buscado):
        
    for Nombre in clientes:
        if Nombre["Nombre"] == Name_Buscado:
            return Nombre        
    return None

'''Se separa la logica de busqueda para añadirlas a la funcion buscar y luego utilizar ambas en la funcion buscar cliente
La función buscar cliente sera utilizada en las funciones actualizar y eliminar cliente'''

def Buscar_cliente(clientes):
    limpiar_pantalla()

    if not clientes: # si no hay registros de clientes se mostrara este mensaje
            print(f"{Azul}\nNo hay usuarios registrados.{Reset}")
            return
    
    while True:
        
        print("Ingreda el nombre o ID del cliente que deseas buscar\n")

        opcion_busqueda = menu_busqueda()

        if opcion_busqueda == "1": #Busqueda por ID
            limpiar_pantalla()
            while True: 

                ID_Buscado = input("\nIngrese el Id del cliente (o escribe 'salir' para volver al menú): ").strip().lower()

                if ID_Buscado == "salir": 
                    print(f"\n{Amarillo}Búsqueda cancelada.{Reset}")
                    break 

                Num_id = busqueda_ID(clientes, ID_Buscado)

                if Num_id:
                    print(f"{bordeC}")
                    print(f"{Verde}Cliente localizado!{Reset}")
                    print(f"{bordeC}")
                    print(f"ID:  {Num_id['ID']}")
                    print(f"Nombre:  {Num_id['Nombre']}")
                    print(f"Edad: {Num_id['Edad']}")
                    print(f"Plan: {Num_id['Plan']}, En estado: {Num_id['Estado']}")
                    print(f"{bordeC}")                
                    return Num_id
                else:
                    print(f"\n{Rojo}Error: El ID de cliente '{ID_Buscado}' no existe.{Reset}")
                    print("Inténtalo de nuevo...\n")
                    continue

        if opcion_busqueda == "2": #Busqueda por Nombre
            limpiar_pantalla()
            while True: 

                Name_Buscado = input("\nIngrese el Nombre del cliente (o escribe 'salir' para volver al menú): ").strip().lower()

                if Name_Buscado == "salir": 
                    print(f"\n{Amarillo}Búsqueda cancelada.{Reset}")
                    break 

                Nombre = busqueda_name(clientes, Name_Buscado)

                if Nombre:
                    print(f"{bordeC}")
                    print(f"{Verde}Cliente localizado!{Reset}")
                    print(f"{bordeC}")
                    print(f"ID:  {Nombre['ID']}")
                    print(f"Nombre:  {Nombre['Nombre']}")
                    print(f"Edad: {Nombre['Edad']}")
                    print(f"Plan: {Nombre['Plan']}, En estado: {Nombre['Estado']}")
                    print(f"{bordeC}")                
                    return Nombre
                else:
                    print(f"\n{Rojo}Error: El nombre de cliente '{Name_Buscado}' no existe.{Reset}")
                    print("Inténtalo de nuevo...\n")
                    continue

        if opcion_busqueda == "3": #Salir
            limpiar_pantalla()
            print(f"\n{Amarillo}Búsqueda cancelada.{Reset}")
            Volviendo()
            break
        