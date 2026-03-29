from OFunciones.aspectos_visuales import *
from OFunciones.Otras_funciones import *
import random

def Crear_cliente(clientes):
    limpiar_pantalla()
    print(f"\n{Verde}Estas creando un nuevo cliente\n{Reset}")

#Nombre
    Exit = ""

    while Exit != 1:
        
        Nombre = input(f"{Azul}Ingrese el nombre del cliente: {Reset}").strip().lower()

        if not Nombre.replace(" ", "").isalpha() or len(Nombre) == 0:
            print(f"{Rojo}Error: El nombre que intentas agregar no es valido.{Reset}")
        
        else:
            print(f"\n{Verde}Nombre de cliente agregado con exito\n{Reset}")
            Exit = 1

#Edad
    back = ""
    while back != 1:
        Edad = input(f"{Azul}Ingrese la edad del cliente: {Reset}")
        if not Edad.isdigit() or int(Edad) <= 0:
            limpiar_pantalla()
            print(f"{Rojo}Error: La Edad debe ser un número mayor a cero.{Reset}")
        else:
            print(f"\n{Verde}Edad de cliente agregada con exito\n{Reset}")
            back = 1
#suscripcion
    salir = ""
    while salir != 1:
        Plan = tipo_plan()

        if Plan == "1":
            print(f"\n{Verde}Plan mensual activado con exito\n{Reset}")
            Plan = "Plan mensual"
            Estado = ("Activo")
            salir = 1
        elif Plan == "2": 
            print(f"\n{Verde}Plan trimestral activado con exito\n{Reset}")
            Plan = "Plan trimestral"
            Estado = ("Activo")
            salir = 1
        elif Plan == "3": 
            print(f"\n{Verde}Plan anual activado con exito\n{Reset}")
            Plan = "Plan anual"
            Estado = ("Activo")
            salir = 1
        else:
            print(f"{Rojo}Opcion invalida, intenta de nuevo.{Reset}")
            continue
    
#numero de ID unico
    while True:
        Num_id = random.randint(1000, 9999)
        if Num_id not in clientes:
            break
    
    Agregando()
    Volviendo()
    return {"ID": int(Num_id), "Nombre": Nombre, "Edad": int(Edad), "Plan": Plan, "Estado": Estado}