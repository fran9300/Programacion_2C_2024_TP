from numeration import getNumberFromSecuence
from entities.utils import getById, clear
from repositories.repository import addEntity, updateEntity, getEntityById, loadData, deleteById
from entities.EntitiesFields import USERS_FIELDS
from entities import EntitiesFields



def getUsers():
    return None

def addUser():
    newUser = {
        "type": "USERS",
        USERS_FIELDS[1]: input("Ingrese el nombre de usuario: "),
        USERS_FIELDS[2]: input("Ingrese el primer nombre: "),
        USERS_FIELDS[3]: input("Ingrese el apellido: "),
        USERS_FIELDS[4]: input("Ingrese la contraseña: "),
        USERS_FIELDS[5]: int(input("Ingrese el nivel de acceso (1=Admin, 2=Usuario): ")),
        USERS_FIELDS[6]: input("Ingrese la fecha de nacimiento (AAAAMMDD): "),
        USERS_FIELDS[7]: input("Ingrese el correo electrónico: "),
        USERS_FIELDS[8]: float(input("Ingrese el saldo inicial: "))
    }
    
    addEntity(newUser)
    print("\nNuevo usuario agregado al sistema.\n")

def editUser():
    userId = int(input("Ingrese el ID del usuario a editar: "))
    userToEdit = getEntityById("USERS", userId)

    if not userToEdit:
        print("No se encontró ningún usuario con ID:", userId)
    else:
        editing = True
        while editing:
            print("\nEditando el usuario:", userToEdit)
            print("Seleccione el campo que desea editar:")
            for key, value in USERS_FIELDS.items():
                print(f"{key}. {value.capitalize()}")
            print("9. Terminar de editar\n")

            choice = int(input("Elige una opción: "))
            if choice == 9:
                editing = False
                print("\nEdición finalizada.")
            elif choice in USERS_FIELDS:
                field = USERS_FIELDS[choice]
                newValue = input(f"Ingrese el nuevo valor para {field}: ")
                userToEdit[field] = newValue
            else:
                print("Opción no válida.")

        # Guardar los cambios en el archivo
        updateEntity(userToEdit)
        print("\nUsuario con ID", userId, "ha sido actualizado en el sistema.\n")

def deleteUser():
    deleteById("USERS")

def printUsers():
    #TODO usar metodo generico
    users = loadData("USERS")  
    print("ID | Nombre de usuario | Nombre | Apellido | Nivel de Acceso | Email | Saldo")
    for user in users:
        if not user.get("deleted", False): 
            print(f"{user['id']} | {user[USERS_FIELDS[1]]} | {user[USERS_FIELDS[2]]} | {user[USERS_FIELDS[3]]} | {user[USERS_FIELDS[5]]} | {user[USERS_FIELDS[7]]} | ${user[USERS_FIELDS[8]]}")
    print()

def checkIfUserExist(userName):
    #Función que chequea si el usuario existe. Como parametro le pasamos el nombre de usuario
    #TODO:REFACTOR que quede como validation
    filtered = list(filter(lambda value : value[1]==userName,getUsers()))
    if(filtered):
        return True
    else:
        return False

def checkUserAndPass(user,password):
    #Función para chequear si el usuario o la clave son correctas

    filtered = list(filter(lambda value : value["username"]==user,loadData(EntitiesFields.USER)))

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
