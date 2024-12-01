import json
from entities.utils import clear
from entities.EntitiesFields import PAYMENT_METHODS, PAYMENT_DISCOUNTS


def configDescuentoPorTipoDePago(metodo):
    """Configura el descuento según el tipo de pago."""
    return PAYMENT_DISCOUNTS.get(metodo, 0.0)

def imprimirDescuentos():
    """Muestra los descuentos actuales para cada método de pago."""
    clear()
    for metodo, descuento in PAYMENT_DISCOUNTS.items():
        print(f"{metodo}: {descuento * 100}% descuento")
    print()

def pedirMetodoDePago():
    """Solicita al usuario seleccionar un método de pago."""
    while True:
        print("\nOpciones de método de pago:")
        for numero, metodo in PAYMENT_METHODS.items():
            print(f"{numero}. {metodo}")
        
        opcion = input("Ingrese el número del método de pago: ")
        if opcion.isdigit() and int(opcion) in PAYMENT_METHODS:
            return int(opcion)
        print("Entrada inválida. Por favor, intente nuevamente.")

def aplicarDescuento(total, metodo_id):
    """Aplica el descuento correspondiente al método de pago."""
    metodo = PAYMENT_METHODS.get(metodo_id)
    descuento = PAYMENT_DISCOUNTS.get(metodo, 0.0)
    return total * (1 - descuento)
