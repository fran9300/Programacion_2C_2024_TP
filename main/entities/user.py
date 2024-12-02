from entities.utils import getById, clear
from repositories.repository import addEntity, updateEntity, getEntityById, loadData, deleteById, printEntities
from entities import EntitiesFields
from entities.EntitiesFields import USERS_FIELDS,USERS_FIELDS_EDIT
from utils.translator import getTranslation

def addUserAdmin(): 
    newUser = {
        "type": "USER",
        USERS_FIELDS[1]:input("Ingrese el Username: "),
        USERS_FIELDS[2]: input("Ingrese el nombre del usuario: "),
        USERS_FIELDS[3]: input("Ingrese el apellido del usuario: "),
        USERS_FIELDS[4]: input("Ingrese la contraseña: "),
        USERS_FIELDS[5]: int(input("Ingrese el rol (1=Admin, 2=Usuario): ")),
        USERS_FIELDS[6]: input("Ingrese el correo electrónico: "),
        EntitiesFields.DELETED : False
    }
    
    addEntity(newUser)
    print("\nNuevo usuario agregado al sistema.\n")


def addUser():
    #Permite agregar nuevos usuarios por parte del administrador  TODO verificaciones
    try:
        newUser = {
            "type": "USER",
            USERS_FIELDS[1]: input("Ingrese nuevo usuario:"),
            USERS_FIELDS[2]: input("Ingrese el nombre del usuario: "),
            USERS_FIELDS[3]: input("Ingrese el apellido del usuario: "),
            USERS_FIELDS[4]: input("Ingrese la contraseña: "),
            USERS_FIELDS[5]: 2,
            USERS_FIELDS[6]: input("Ingrese el correo electrónico: "),
            EntitiesFields.DELETED : False
        }
        confirmacion = int(input("\npresione 1 para confirmar, 0 para cancelar: "))
        if confirmacion == 1:
            userId = addEntity(newUser)
            nuevoSaldo = {"type": EntitiesFields.PAYMENT_METHODS,EntitiesFields.USER_PAYMENT_USER_ID:userId,
                                    EntitiesFields.USER_PAYMENT_CASH:1,EntitiesFields.USER_PAYMENT_TRANSFER:1,
                                    EntitiesFields.USER_PAYMENT_DEBIT:1,EntitiesFields.USER_PAYMENT_CREDIT:1,
                                    EntitiesFields.USER_PAYMENT_POINTS:1,EntitiesFields.DELETED:False}
            addEntity(nuevoSaldo)
            print("\nNuevo usuario agregado al sistema.\n")
        else:
            print("\noperacion cancelada\n")
    except Exception as e: 
        print("Error inesperado ingresando usuario")

def editUser():
    #permite editar usuarios existentes
    try:
        printEntities(EntitiesFields.USER)
        userId = int(input("Ingrese el ID del usuario a editar: "))
        userToEdit = getEntityById(EntitiesFields.USER, userId)

        if not userToEdit:
            print("No se encontró ningún usuario con ID:", userId)
        else:
            editing = True
            while editing:
                print("\nEditando el usuario:", userToEdit)            
                print("Seleccione el campo que desea editar:")
                for index in range(1, len(USERS_FIELDS)):
                    field = USERS_FIELDS[index]
                    field = getTranslation(field)
                    print(f"{index}. {field}")
                print(f"{len(USERS_FIELDS)}. Terminar de editar\n")

                choice = int(input("Elige una opción: "))
                if choice == len(USERS_FIELDS):
                    editing = False
                    print("\nEdición finalizada.")
                elif 1 <= choice < len(USERS_FIELDS):
                    field = USERS_FIELDS[choice]
                    fieldTrans = getTranslation(field)
                    newValue = input(f"Ingrese el nuevo valor para {fieldTrans}: ")
                    userToEdit[field] = newValue
                else:
                    print("Opción no válida.")
            # Guardar los cambios en el archivo
            userToEdit[EntitiesFields.TYPE] = EntitiesFields.USER
            updateEntity(userToEdit)
            print("\nUsuario con ID", userId, "ha sido actualizado en el sistema.\n")
    except ValueError:
        print("valor mal introducido, por favor ingrese los mismos segun lo indicado en pantalla\n")


def deleteUser():
    #permite borrar usuarios existentes, utilizando la funcion genérica deleteById
    deleteById(EntitiesFields.USER)


def printUsers():
    #permite imprimir usuarios existentes, utilizando la funcion genérica printEntities
    printEntities(EntitiesFields.USER)


def checkUserAndPass(user,password):
    #Función para chequear si el usuario o la clave son correctas

    filtered = list(filter(lambda value : value["userName"]==user,loadData(EntitiesFields.USER)))

    if len(filtered) == 0:
        clear()
        print("\nUsuario o contraseña incorrecta, intente nuevamente\n")
        return None 

    user = filtered[0]
    if(user["password"] == password):
        return user
    else:
        clear()
        print("\nUsuario o contraseña incorrecta, intente nuevamente\n")
