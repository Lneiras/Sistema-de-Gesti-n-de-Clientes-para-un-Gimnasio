from OFunciones.aspectos_visuales import *
from OFunciones.Otras_funciones import *
from Funciones_CRUD.Buscar_usuario import *


def Actualizar_cliente(clientes):
    limpiar_pantalla()
    if not clientes: #Si el usuario consulta esta opción sin tener productos en el inventario se mostrara ese mensaje
        print(f"{Azul}\nNo hay usuarios registrados.{Reset}")
        return

    while True:

        User = Buscar_cliente(clientes)

        '''En esta parte nos aseguramos que si en la funsión "Buscar_clientes" el usuario escribe 'salir' y devuelve un valor None
        con el 'return' la función se cierra sin pasar a la siguiente parte de la función'''

        if User is None:
            print(f"\n{Amarillo}Operación de actualización cancelada.{Reset}")
            return
    
        opcion_Actualizar = menu_actualizacion()

        if opcion_Actualizar == "1": #Actualizar Tipo de plan
            print("Selecciona el nuevo plan\n")
            salir = ""
            while salir != 1:
                nuevo_plan = tipo_plan()

                '''En este caso se realiza la creación de un diccionario con los planes disponibles para que fuese más sencillo realizar.
                Las validaciones y, si es necesario, posteriormente realizar cambios en estos planes o agregar más sin tener que reestructurar mucho del código.'''
                planes = {
                            "1": "Plan mensual",
                            "2": "Plan trimestral",
                            "3": "Plan anual"
                        }

                if nuevo_plan in planes:
                    seleccion = planes[nuevo_plan]
                    
                    if User["Plan"] == seleccion:
                        print(f"\n{Rojo}Error: El usuario ya tiene el '{seleccion}'.{Reset}")
                        print("Por favor, selecciona un plan diferente o escribe 'salir'.")
                        continue 
                    
                    User["Plan"] = seleccion
                    print(f"\n{Verde}{seleccion} activado con éxito!{Reset}")
                    Volviendo()
                    salir = 1

                else:
                    print(f"{Rojo}Opción inválida.{Reset}")
                    continue


        elif opcion_Actualizar == "2": #Actualizar Estado plan
            Cargando()
            salir = ""
            while salir != 1:
                    
                Estado = User["Estado"]

                if Estado.lower() == "activo":
                    User["Estado"] = "inactivo"
                    salir = 1
                
                elif Estado.lower() == "inactivo":
                    User["Estado"] = "activo"
                    salir = 1
                    
            print(f"\n{Verde}Cambio en el estado del plan realizado con exito{Reset}")
            Volviendo()

        elif opcion_Actualizar == "3": #salir
            print(f"\n{Amarillo}Operación de actualización cancelada.{Reset}")
            Volviendo()
            break
        
        else:
            print(f"\n{Rojo}Error: opcion no valida{Reset}")
            print("Inténtalo de nuevo...\n")
            continue