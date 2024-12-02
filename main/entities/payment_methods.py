# payment_methods.py

import json
from entities.EntitiesFields import *
from entities import EntitiesFields
from repositories.repository import printEntities,updateEntity,getEntityByProperties,printCustomEntities,getEntityById
from entities.utils import clear
from utils.translator import getTranslation

DESCUENTOS_PATH = "main/repositories/files/descuentos.json"  # Archivo JSON para descuentos

def cargarDescuentos():
    """Carga los descuentos desde un archivo JSON."""
    try:
        with open(DESCUENTOS_PATH, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {metodo: 0.0 for metodo in PAYMENT_METHODS.values()}

def guardarDescuentos(descuentos):
    """Guarda los descuentos en un archivo JSON."""
    with open(DESCUENTOS_PATH, "w") as file:
        json.dump(descuentos, file, indent=4)



def aplicarDescuento(total, metodo_name):
    """Aplica el descuento correspondiente al método de pago."""
    print(EntitiesFields.PAYMENT_METHODS(metodo_name))
    metodo = EntitiesFields.PAYMENT_METHODS[metodo_name]
    descuentos = cargarDescuentos()
    descuento = descuentos.get(metodo, 0.0)
    return total * (1 - descuento)


def configurarDescuentos():
        #permite editar los descuentos
    try:
        printEntities(EntitiesFields.PAYMENT_METHODS)
        discounts = getEntityById(EntitiesFields.PAYMENT_METHODS, 1)

        if not discounts:
            print("No se encontró ningún descuento\n")
        else:
            editing = True
            while editing:
                print("\nEditando los descuentos:", discounts)            
                print("Seleccione el campo que desea editar:")
                for index in range(0, len(PAYMENT_METHODS_FIELDS)):
                    field = PAYMENT_METHODS_FIELDS[index]
                    field = getTranslation(field)
                    print(f"{index}. {field}")
                print(f"{len(PAYMENT_METHODS_FIELDS)}. Terminar de editar\n")

                choice = int(input("Elige una opción: "))
                if choice == len(PAYMENT_METHODS_FIELDS):
                    editing = False
                    print("\nEdición finalizada.")
                elif 1 <= choice < len(PAYMENT_METHODS_FIELDS):
                    field = PAYMENT_METHODS_FIELDS[choice]
                    fieldTrans = getTranslation(field)
                    newValue = float(input(f"Ingrese el nuevo valor para {fieldTrans}: "))
                    discounts[field] = newValue
                else:
                    print("Opción no válida.")
            # Guardar los cambios en el archivo
            discounts[EntitiesFields.TYPE] = EntitiesFields.PAYMENT_METHODS
            updateEntity(discounts)
            print("\nDescuentos actualizados\n")
    except ValueError:
        print("valor mal introducido, por favor ingrese los mismos segun lo indicado en pantalla\n")


def imprimirDescuentos():
    descuentos = getEntityByProperties(PAYMENT_METHODS,[ID],1)
    clear()
    printEntities(EntitiesFields.PAYMENT_METHODS)


    """def configurarDescuentos2():
    #Permite al administrador configurar los descuentos.
    descuentos = cargarDescuentos()
    print("\nConfiguración de descuentos:")
    for metodo, descuento in descuentos.items():
        print(f"{metodo}: {descuento * 100}% descuento actual")
        nuevo_descuento = input(f"Ingrese el nuevo porcentaje de descuento para {metodo} (o presione Enter para dejar igual): ")
        if nuevo_descuento.strip():
            try:
                nuevo_descuento = float(nuevo_descuento) / 100
                if 0 <= nuevo_descuento <= 1:
                    descuentos[metodo] = nuevo_descuento
                else:
                    print("El descuento debe estar entre 0% y 100%.")
            except ValueError:
                print("Por favor, ingrese un valor numérico válido.")
    guardarDescuentos(descuentos)
    print("\nDescuentos actualizados correctamente.")
    
    
    def imprimirDescuentos2():
    #Muestra los descuentos actuales para cada método de pago.
    descuentos = cargarDescuentos()
    clear()
    print("\nDescuentos configurados: \n")
    for metodo, descuento in descuentos.items():
        print(f"{metodo}: {descuento * 100}% descuento")
    print()
    
    
    """