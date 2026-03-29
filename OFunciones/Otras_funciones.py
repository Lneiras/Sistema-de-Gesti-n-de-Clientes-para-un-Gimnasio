from OFunciones.aspectos_visuales import *

def menu():
    
    print(f"{Magenta}┌{bordeC}┐")
    print(f"│{Blanco}{"1. Crear cliente":<{AnchoC}}{Reset}{Magenta}│")
    print(f"│{Blanco}{"2. Listar clientes":<{AnchoC}}{Reset}{Magenta}│")
    print(f"│{Blanco}{"3. Buscar cliente":<{AnchoC}}{Reset}{Magenta}│")
    print(f"│{Blanco}{"4. Actualizar cliente":<{AnchoC}}{Reset}{Magenta}│")
    print(f"│{Blanco}{"5. Eliminar cliente":<{AnchoC}}{Reset}{Magenta}│")
    print(f"│{Blanco}{"6. Salir":<{AnchoC}}{Reset}{Magenta}│")
    print(f"└{bordeC}┘{Reset}")

    
    opcion = input(f"{Blanco}\nIngresa la opción deseada: ")
    return opcion


def salir(): #Función de salida, encargada de cerrar el programa
    Saliendo()
    lineasalida = "Gracias por usar el sistema de gestión de Clientes"
    print(f"\n{Azul}┌{bordeP}┐")
    print(f"│{lineasalida:^{AnchoP}}│")
    print(f"└{bordeP}┘{Reset}\n")

def menu_busqueda():
    print(f"{Cian}┌{bordeC}┐")
    print(f"│{Blanco}{"1. Busqueda por ID":<{AnchoC}}{Reset}{Cian}│")
    print(f"│{Blanco}{"2. Busqueda Por nombre":<{AnchoC}}{Reset}{Cian}│")
    print(f"│{Blanco}{"3. Salir":<{AnchoC}}{Reset}{Cian}│")
    print(f"└{bordeC}┘{Reset}")
    
    opcion_busqueda = input(f"{Blanco}\nIngresa la opción deseada: ")
    return opcion_busqueda

def menu_actualizacion():
    print(f"{Cian}┌{bordeC}┐")
    print(f"│{Blanco}{"1. Actualizar Tipo de plan":<{AnchoC}}{Reset}{Cian}│")
    print(f"│{Blanco}{"2. Actualizar Estado":<{AnchoC}}{Reset}{Cian}│")
    print(f"│{Blanco}{"3. Salir":<{AnchoC}}{Reset}{Cian}│")
    print(f"└{bordeC}┘{Reset}")
    
    opcion_Actualizar = input(f"{Blanco}\nIngresa la opción deseada: ")
    return opcion_Actualizar

def tipo_plan():
    print(f"{Cian}┌{bordeC}┐")
    print(f"│{Blanco}{"1. Plan Mensual":<{AnchoC}}{Reset}{Cian}│")
    print(f"│{Blanco}{"2. Plan trimestral":<{AnchoC}}{Reset}{Cian}│")
    print(f"│{Blanco}{"3. Plan anual":<{AnchoC}}{Reset}{Cian}│")
    print(f"└{bordeC}┘{Reset}")

    Plan = input(f"{Blanco}\nIngresa la opción deseada: ")
    return Plan