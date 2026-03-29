
Lista_clientes = []


import csv
import os

Clientes_csv = os.path.join('Data', 'Clientes_csv')

def guardar_datos_csv(Clientes_csv, Lista_clientes):
    try:
        with open(Clientes_csv, mode='w', newline='', encoding='utf-8') as archivo:
            campos = ["ID", "Nombre", "Edad", "Plan", "Estado"]
            writer = csv.DictWriter(archivo, fieldnames=campos)
            
            writer.writeheader()
            writer.writerows(Lista_clientes)
        return True
    
    except Exception as e:
        print(f"Error al guardar: {e}")
        return False

def cargar_datos_csv(Clientes_csv ):
    Lista_clientes = []
    try:
        with open(Clientes_csv , mode='r', encoding='utf-8') as archivo:
            reader = csv.DictReader(archivo)
            for fila in reader:
                Lista_clientes.append(fila)
        return Lista_clientes
    except FileNotFoundError:
        return []
    # Si el archivo no existe, retornamos una lista vacía para empezar de cero