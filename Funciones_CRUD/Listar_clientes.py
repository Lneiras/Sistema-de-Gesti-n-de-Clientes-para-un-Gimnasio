from OFunciones.aspectos_visuales import *


def Listar_clientes(clientes):
    Cargando()

    if not clientes: # si no hay registros de clientes se mostrara este mensaje
        print(f"{Azul}\nNo hay usuarios registrados.{Reset}")
        return
    limpiar_pantalla()
    LineaL = "Lista de clientes"
    print(f"{bordeL}")
    print(f"{Verde}{LineaL:^{AnchoL}}{Reset}")
    print(f"{bordeL}")
    print(f"{'ID':<6} | {'Nombre':<16} | {'Edad':<6} | {'Plan':<16} | {'Estado':<9}")
    print(f"{bordeL}")

    for i in clientes:
        print(f"{i['ID']:<6} | {i['Nombre']:<16} | {i['Edad']:<6} | {i['Plan']:<16} | {i['Estado']:<9}")
    Volviendo()