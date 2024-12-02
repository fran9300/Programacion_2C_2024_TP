import json
from entities.EntitiesFields import *
from entities import EntitiesFields
from entities.utils import clear
from utils.translator import getTranslation
from entities.payment_methods import aplicarDescuento
from repositories.repository import printEntities,updateEntity,getEntityByProperties,printCustomEntities,getEntityById,listByProperties

def listarSaldos(user_id):
    """Lista los saldos disponibles para un usuario."""
    saldo = listByProperties(EntitiesFields.USER_PAYMENT,[EntitiesFields.USER_PAYMENT_USER_ID,EntitiesFields.DELETED],user_id,False)
    print(f"\nSaldos disponibles para el usuario {user_id}:\n")
    printCustomEntities(saldo,USER_PAYMENT)
    print()

def cargarSaldo(userId):
        #permite editar los saldos
    try:
        listarSaldos(userId)
        paymentBalance = getEntityByProperties(EntitiesFields.USER_PAYMENT,[EntitiesFields.USER_PAYMENT_USER_ID], userId)

        if not paymentBalance:
            print("No se encontró ningún metodo de pago\n")
        else:
            editing = True
            while editing:
                #print("\nEditando los balances:", paymentBalance)
                clear()
                listarSaldos(userId)            
                print("Seleccione el campo que desea editar:")
                for index in range(1, len(USER_PAYMENT_FIELDS_EDIT)):
                    field = USER_PAYMENT_FIELDS_EDIT[index]
                    field = getTranslation(field)
                    print(f"{index}. {field}")
                print(f"{len(USER_PAYMENT_FIELDS_EDIT)}. Terminar de editar\n")

                choice = int(input("Elige una opción: "))
                if choice == len(USER_PAYMENT_FIELDS_EDIT):
                    editing = False
                    print("\nEdición finalizada.")
                elif 1 <= choice < len(USER_PAYMENT_FIELDS_EDIT):
                    field = USER_PAYMENT_FIELDS_EDIT[choice]
                    fieldTrans = getTranslation(field)
                    newValue = float(input(f"Ingrese el nuevo valor para {fieldTrans}: "))
                    paymentBalance[field] = newValue
                else:
                    print("Opción no válida.")
                    clear()
            # Guardar los cambios en el archivo
            paymentBalance[EntitiesFields.TYPE] = EntitiesFields.USER_PAYMENT
            updateEntity(paymentBalance)
            print("\nBalances actualizados\n")
    except ValueError:
        print("valor mal introducido, por favor ingrese los mismos segun lo indicado en pantalla\n")

def pagarConSaldo(currentUserId,monto):
    #Función para pagar una cantidad específica usando saldo.
    # Aquí puedes pedir el monto al usuario o dejarlo como ejemplo fijo
    #monto = float(input("Ingrese el monto a pagar: "))
    valor = elegirMetodoPago(currentUserId, monto)
    return valor

def elegirMetodoPago(user_id, total):
    #Permite al usuario elegir un método de pago para realizar una transacción.
    payments = getEntityByProperties(EntitiesFields.USER_PAYMENT,[EntitiesFields.USER_PAYMENT_USER_ID,EntitiesFields.DELETED],user_id,False)
    listarSaldos(user_id)

    print("Seleccione un metodo de pago:\n")

    if not payments:
        print("No se encontró ningún metodo de pago\n")
    else:
        selecting = True
        while selecting:
            #print("\nEditando los balances:", paymentBalance)
            clear()
            listarSaldos(user_id)            
            print("Seleccione el campo que desea editar:")
            for index in range(1, len(USER_PAYMENT_FIELDS_EDIT)):
                field = USER_PAYMENT_FIELDS_EDIT[index]
                field = getTranslation(field)
                print(f"{index}. {field}")
            print(f"{len(USER_PAYMENT_FIELDS_EDIT)}. Terminar de editar\n")

            choice = int(input("Elige una opción: "))
            if choice == len(USER_PAYMENT_FIELDS_EDIT):
                selecting = False
                print("\nSelección confirmada.")
            elif 1 <= choice < len(USER_PAYMENT_FIELDS_EDIT):
                seleccion = USER_PAYMENT_FIELDS_EDIT[choice]
                fieldTrans = getTranslation(seleccion)
                print(f"Selección actual: {fieldTrans}")
                selecting = False
            else:
                print("Opción no válida.")
                clear()

    #totalConDescuento = aplicarDescuento(total, seleccion)
    totalConDescuento = total

    if payments["user_idBalance"] == user_id:
        if payments[seleccion] >= totalConDescuento:
            payments[seleccion] -= totalConDescuento
            field = USER_PAYMENT_FIELDS_EDIT[choice]
            newValue = payments[seleccion]
            payments[field] = newValue
            payments[EntitiesFields.TYPE] = EntitiesFields.USER_PAYMENT
            updateEntity(payments)
            clear()
            #print(f"Pago realizado exitosamente con {PAYMENT_METHODS[seleccion]}. Saldo restante: {payments[seleccion]}")
            return True,user_id, totalConDescuento
        else:
            #clear()
            print("Saldo insuficiente. Intente nuevamente.")
            return False,user_id, totalConDescuento
    print("Método de pago no encontrado o sin saldo disponible.")


"""
def listarSaldos2(user_id):
    #Lista los saldos disponibles para un usuario.
    payments = cargarUserPayments()
    print(f"\nSaldos disponibles para el usuario {user_id}:\n")
    for payment in payments:
        if payment["user_id"] == user_id:
            metodo = PAYMENT_METHODS.get(payment["payment_type"], "Desconocido")
            print(f"- {metodo}: {payment['balance']} créditos")
    print()


def elegirMetodoPago(user_id, total):
    #Permite al usuario elegir un método de pago para realizar una transacción.
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
    #Función para pagar una cantidad específica usando saldo.
    # Aquí puedes pedir el monto al usuario o dejarlo como ejemplo fijo
    #monto = float(input("Ingrese el monto a pagar: "))
    valor = elegirMetodoPago(currentUserId, monto)
    return valor

def cargarSaldo2(user_id):
    #Permite al usuario cargar saldo en un método de pago específico.
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

"""