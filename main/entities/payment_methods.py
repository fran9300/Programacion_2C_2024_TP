# payment_methods.py

import json
from entities.EntitiesFields import PAYMENT_METHODS

DESCUENTOS_PATH = "main/repositories/descuentos.json"  # Archivo JSON para descuentos

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

def imprimirDescuentos():
    """Muestra los descuentos actuales para cada método de pago."""
    descuentos = cargarDescuentos()
    print("\nDescuentos configurados:")
    for metodo, descuento in descuentos.items():
        print(f"{metodo}: {descuento * 100}% descuento")
    print()

def aplicarDescuento(total, metodo_id):
    """Aplica el descuento correspondiente al método de pago."""
    metodo = PAYMENT_METHODS.get(metodo_id)
    descuentos = cargarDescuentos()
    descuento = descuentos.get(metodo, 0.0)
    return total * (1 - descuento)
