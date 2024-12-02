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

def configurarDescuentos():
    """Permite al administrador configurar los descuentos."""
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