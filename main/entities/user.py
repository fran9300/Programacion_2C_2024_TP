from numeration import getNumberFromSecuence
users= [
    [1,"fpelli","Franco","Pelli","contraseña",2,"20020325","fpelli@uade.edu.ar",100000],
    [2,"ipelli","Ivan","Pelli","contraseña123",2,"20061010","ipelli@uade.edu.ar",50000],
    [3,"admin","","","admin",1,"20000101","admin@uade.edu.ar",100000]
]


def getUsers():
    return users

def addUser():
    global users
    newUser = []
    newUser.append(getNumberFromSecuence("userNumeration"))
    print("Ingrese nombre de usuario")
    newUser.append(input())
    print("Ingrese nombre")
    newUser.append(input())
    print("Ingrese apellido")
    newUser.append(input())
    newUser.append(2) ## le agrega el rol
    print("Ingrese contraseña")
    newUser.append(input())    
    print("Ingrese fecha de nacimiento(formato YYYYMMDD)")
    newUser.append(input())
    print("Ingrese correo electronico")
    newUser.append(input())
    print("Ingrese saldo")
    newUser.append(int(input()))
    print(newUser)
    users.append(newUser)
    print("Nuevo usuario agregado")

def checkUserAndPass(user,password):
    filtered = list(filter(lambda value : value[1]==user,getUsers()))
    user = filtered[0]
    if(user[4] == password):
        return user
    else:
        print("Usuario o contraseña incorrecta")
