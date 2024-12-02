import json
from entities.EntitiesFields import *
from entities.utils import clear
from entities.payment_methods import aplicarDescuento

  # Archivo JSON para datos de saldo
USER_PAYMENT_PATH = "main/repositories/files/user_payment.json"

def cargarUserPayments():
    """Carga los registros de pagos de usuarios desde el archivo JSON."""
    try:
        with open(USER_PAYMENT_PATH, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def guardarUserPayments(payments):
    """Guarda los registros de pagos de usuarios en el archivo JSON."""
    with open(USER_PAYMENT_PATH, "w") as file:
        json.dump(payments, file, indent=4)

def listarSaldos(user_id):
    """Lista los saldos disponibles para un usuario."""
    payments = cargarUserPayments()
    print(f"\nSaldos disponibles para el usuario {user_id}:\n")
    for payment in payments:
        if payment["user_id"] == user_id:
            metodo = PAYMENT_METHODS.get(payment["payment_type"], "Desconocido")
            print(f"- {metodo}: {payment['balance']} créditos")
    print()

def cargarSaldo(user_id):
    """Permite al usuario cargar saldo en un método de pago específico."""
    payments = cargarUserPayments()
    listarSaldos(user_id)
    clear()
    print("\nOpciones de método de pago:\n")
    for key, value in PAYMENT_METHODS.items():
        print(f"{key}. {value}")
    metodo_id = int(input("\nSeleccione el ID del método de pago para cargar saldo: \n"))

    monto = float(input("Ingrese el monto a cargar: "))
    for payment in payments:
        if payment["user_id"] == user_id and payment["payment_type"] == metodo_id:
            payment["balance"] += monto
            guardarUserPayments(payments)
            clear()
            print(f"Saldo actualizado. Nuevo saldo para {PAYMENT_METHODS[metodo_id]}: {payment['balance']}")
            return

    nuevo_registro = {"id": len(payments) + 1, "user_id": user_id, "payment_type": metodo_id, "balance": monto}
    payments.append(nuevo_registro)
    guardarUserPayments(payments)
    print(f"Saldo cargado en el nuevo método de pago {PAYMENT_METHODS[metodo_id]}: {monto}")

def elegirMetodoPago(user_id, total):
    """Permite al usuario elegir un método de pago para realizar una transacción."""
    payments = cargarUserPayments()
    listarSaldos(user_id)

    # Listar métodos de pago con sus IDs
    print("\nMétodos de pago disponibles:")
    for metodo_id, metodo_nombre in PAYMENT_METHODS.items():
        print(f"{metodo_id}: {metodo_nombre}")

    metodo_id = int(input("\nSeleccione el ID del método de pago para usar: "))

    totalConDescuento = aplicarDescuento(total, metodo_id)

    for payment in payments:
        if payment["user_id"] == user_id and payment["payment_type"] == metodo_id:
            if payment[USER_PAYMENT_BALANCE] >= totalConDescuento:
                payment[USER_PAYMENT_BALANCE] -= totalConDescuento
                guardarUserPayments(payments)
                clear()
                print(f"Pago realizado exitosamente con {PAYMENT_METHODS[metodo_id]}. Saldo restante: {payment['balance']}")
                return True, totalConDescuento
            else:
                clear()
                print("Saldo insuficiente. Intente nuevamente.")
                return False
    print("Método de pago no encontrado o sin saldo disponible.")

def pagarConSaldo(currentUserId,monto):
    """Función para pagar una cantidad específica usando saldo."""
    # Aquí puedes pedir el monto al usuario o dejarlo como ejemplo fijo
    #monto = float(input("Ingrese el monto a pagar: "))
    valor = elegirMetodoPago(currentUserId, monto)
    return valor