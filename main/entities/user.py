from numeration import getNumberFromSecuence
from entities.utils import getById, clear
from repositories.repository import addEntity, updateEntity, getEntityById, loadData, deleteById, printEntities
from entities import EntitiesFields


def getUsers():
    return None

def addUser():
    newUser = {
        EntitiesFields.TYPE: EntitiesFields.USER,
        EntitiesFields.USER_USERNAME: input("Ingrese el nombre de usuario: "),
        EntitiesFields.USER_FIRST_NAME: input("Ingrese el primer nombre: "),
        EntitiesFields.USER_LAST_NAME: input("Ingrese el apellido: "),
        EntitiesFields.USER_PASSWORD: input("Ingrese la contraseña: "),
        EntitiesFields.USER_ACCESS_LEVEL: int(input("Ingrese el nivel de acceso (1=Admin, 2=Usuario): ")),
        EntitiesFields.USER_BIRTHDATE: input("Ingrese la fecha de nacimiento (AAAAMMDD): "),
        EntitiesFields.USER_EMAIL: input("Ingrese el correo electrónico: "),
        EntitiesFields.USER_BALANCE: float(input("Ingrese el saldo inicial: "))
    }
    
    addEntity(newUser)
    print("\nNuevo usuario agregado al sistema.\n")

from entities import EntitiesFields
from repositories.repository import getEntityById, updateEntity

def editUser():
    userId = int(input("Ingrese el ID del usuario a editar: "))
    userToEdit = getEntityById(EntitiesFields.USER, userId)

    if not userToEdit:
        print("No se encontró ningún usuario con ID:", userId)
    else:
        editing = True
        while editing:
            print("\nEditando el usuario:", userToEdit)
            print("Seleccione el campo que desea editar:")
            print("1. Nombre de usuario")
            print("2. Primer nombre")
            print("3. Apellido")
            print("4. Contraseña")
            print("5. Nivel de acceso")
            print("6. Fecha de nacimiento")
            print("7. Correo electrónico")
            print("8. Saldo")
            print("9. Terminar de editar\n")

            choice = int(input("Elige una opción: "))
            if choice == 9:
                editing = False
                print("\nEdición finalizada.")
            else:
                # Mapa de opciones a los campos correspondientes en EntitiesFields
                field_map = {
                    1: EntitiesFields.USER_USERNAME,
                    2: EntitiesFields.USER_FIRST_NAME,
                    3: EntitiesFields.USER_LAST_NAME,
                    4: EntitiesFields.USER_PASSWORD,
                    5: EntitiesFields.USER_ACCESS_LEVEL,
                    6: EntitiesFields.USER_BIRTHDATE,
                    7: EntitiesFields.USER_EMAIL,
                    8: EntitiesFields.USER_BALANCE
                }

                if choice in field_map:
                    field = field_map[choice]
                    newValue = input(f"Ingrese el nuevo valor para {field}: ")
                    
                    # Validación de tipo para ciertos campos
                    if field == EntitiesFields.USER_ACCESS_LEVEL:
                        try:
                            newValue = int(newValue)
                        except ValueError:
                            print("Nivel de acceso inválido. Debe ser un número entero.")
                            continue
                    elif field == EntitiesFields.USER_BALANCE:
                        try:
                            newValue = float(newValue)
                        except ValueError:
                            print("Saldo inválido. Debe ser un número.")
                            continue
                    
                    # Actualizar el campo seleccionado
                    userToEdit[field] = newValue
                else:
                    print("Opción no válida.")

        # Guardar los cambios en el archivo
        updateEntity(userToEdit)
        print("\nUsuario con ID", userId, "ha sido actualizado en el sistema.\n")


def deleteUser():
    userId = int(input("Ingrese el ID del usuario que desea eliminar: "))
    if deleteById(EntitiesFields.USER, userId):
        print(f"\nUsuario con ID {userId} ha sido eliminado del sistema.\n")
    else:
        print(f"No se encontró ningún usuario con ID: {userId}")


def printUsers():
    printEntities(EntitiesFields.USER)



def checkUserAndPass(username, password):
    # Función para chequear si el usuario o la clave son correctas
    users = getUsers()
    filtered_users = [user for user in users if user[EntitiesFields.USER_USERNAME] == username]

    if not filtered_users:
        clear()
        print("\nUsuario o contraseña incorrecta, intente nuevamente\n")
        return None

    user = filtered_users[0]
    if user[EntitiesFields.USER_PASSWORD] == password:
        return user
    else:
        clear()
        print("\nUsuario o contraseña incorrecta, intente nuevamente\n")
        return None
