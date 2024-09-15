from numeration import getNumberFromSecuence
from utils import getById

users= [
    [1,"fpelli","Franco","Pelli","contraseña",2,"20020325","fpelli@uade.edu.ar",100000],
    [2,"ipelli","Ivan","Pelli","contraseña123",2,"20061010","ipelli@uade.edu.ar",50000],
    [3,"admin","","","admin",1,"20000101","admin@uade.edu.ar",100000]
]


def getUsers():
    return users


#Función para agregar usuario
def addUser():
    global users
    newUser = []
    newUser.append(getNumberFromSecuence("userNumeration"))
    print("Ingrese nombre de usuario")
    userName = input()
    while checkIfUserExist(userName):
        print("Nombre de usuario no disponible, ingrese otro")
        userName = input()
    newUser.append(userName)
    print("Ingrese nombre")
    newUser.append(input())
    print("Ingrese apellido")
    newUser.append(input())
    print("Ingrese contraseña")
    newUser.append(input())    
    newUser.append(2) ## le agrega el rol
    print("Ingrese fecha de nacimiento(formato YYYYMMDD)")
    newUser.append(input())
    print("Ingrese correo electronico")
    newUser.append(input())
    print("Ingrese saldo")
    newUser.append(int(input()))    
    users.append(newUser)
    print("Nuevo usuario agregado")
    print(users)


#Función que chequea si el usuario existe. Como parametro le pasamos el nombre de usuario
def checkIfUserExist(userName):
    filtered = list(filter(lambda value : value[1]==userName,getUsers()))
    if(filtered):
        return True
    else:
        return False

#Función para chequear si el usuario o la clave son correctas
def checkUserAndPass(user,password):
    filtered = list(filter(lambda value : value[1]==user,getUsers()))
    user = filtered[0]
    if(user[4] == password):
        return user
    else:
        print("Usuario o contraseña incorrecta")


#Función para editar usuarios. Le pasamos la matriz users. Puede editar mas de un campo a la vez y
#finalizar la edicion cuando el usuario lo desee
def editUser(users):
  
    print("Ingrese el ID del usuario que desea editar:")
    user_id = int(input())

    user = None
    for u in users:
        if u[0] == user_id:
            user = u
    
    if not user:
        print("Usuario no encontrado.")
    else:
        bandera=True
        while bandera: 
            print("Seleccione el campo que desea editar:")
            print("1. Nombre de usuario")
            print("2. Nombre")
            print("3. Apellido")
            print("4. Contraseña")
            print("5. Fecha de nacimiento")
            print("6. Correo electrónico")
            print("7. Saldo")
            print ("8. Finalizar la edición")

            choice = int(input())

            if choice == 1:
                print("Ingrese el nuevo nombre de usuario:")
                user[1] = input()
            elif choice == 2:
                print("Ingrese el nuevo nombre:")
                user[2] = input()
            elif choice == 3:
                print("Ingrese el nuevo apellido:")
                user[3] = input()
            elif choice == 4:
                print("Ingrese la nueva contraseña:")
                user[4] = input()
            elif choice == 5:
                print("Ingrese la nueva fecha de nacimiento (formato YYYYMMDD):")
                user[6] = input()
            elif choice == 6:
                print("Ingrese el nuevo correo electrónico:")
                user[7] = input()
            elif choice == 7:
                print("Ingrese el nuevo saldo:")
                user[8] = int(input())
            elif choice==8:
                bandera=False
                print ("Ha finalizado la edición")
            else:
                print("Opción no válida.")
                return

    print("Datos del usuario actualizados:", user)


#Función para eliminar usuario. Reutilizamos la función getById
def deleteUser(usuarioId, usuarios):
    userToDelete = getById(usuarioId, usuarios)
    
    if userToDelete == -1:
        print("No se encontró ningún usuario con ID: ", usuarioId)
    else:
        users.remove(userToDelete)
        print("Usuario con ID ",usuarioId, "ha sido eliminado.")

    return users



#Programa principal:
#print (editUser(users))

