
from entities.movies import addMovie,printMovies,deleteMovie,editMovie
from entities.user import getUsers, addUser, editUser, deleteUser,printUsers, checkUserAndPass,NewUser
from entities.reservation import addReservation, checkReservations, valorEntrada, checkRoom
from entities.utils import clear
from entities.room import addRoom, printRooms
from entities.room_configuration import addRoomConfiguration
import os
import re
from repositories.repository import getEntityByProperties,initDefaultValues,printEntities, deleteById, EntitiesFields


#Arrays y variables con datos hardcodeados ----------------------------------------------------------------------------------------

currentMenu = {}
mainMenu = {}
currentUserId = ""

roles = [
    [1,"admin"],
    [2,"client"]
]

# [id,userId,metodoDePagoId]
userPayment = [
    [1,1,1],
    [2,1,3],
    [3,2,2]
]

descuentos = {
    "Cash": 0.30,     # 30% descuento
    "Transfer": 0.20, # 20% descuento
    "Debt": 0.10,     # 10% descuento
    "Credit": 0.02,   # 2% descuento
    # Para "Points" se manejará en una función aparte
}

METODOS_DE_PAGO = {
    1: "Cash",
    2: "Transfer",
    3: "Debt",
    4: "Credit",
    5: "Points"
}

#-----------------------------------------------------------------------------------------------------------------------------------------

def VerificarPrecioEntrada():
    global valorEntrada
    clear()
    print(f"\nvalor actual de la entrada de cine: {valorEntrada}\n")

def ModificarValorEntrada():
    #TODO cambiar a entidad para poder guardarla en un archivo json
    global valorEntrada
    VerificarPrecioEntrada()
    try:
        valorEntrada = float(input("ingrese el valor de la entrada estandar de cine: "))
        confirmacion = int(input("\npresione 1 para confirmar, 0 para cancelar: "))
    except ValueError:
        clear()
        print("valor incorrecto, ingrese un numero con . para el precio de la entrada\n")
    else:
        clear()
        if confirmacion == 1:
            print("\rprecio de la entrada actualizado correctamente\n")
        else:
            print("\noperacion cancelada\n")

#Funciones para el manejo de las películas------------------------------------------------------------------------------------------------


def loadMovie():
    #Función para cargar una nueva película en el sistema
    clear()
    addMovie()
    return None

def viewMovies():
    #Función para consultar y mostrar la lista de películas disponibles en el sistema
    clear()
    printMovies()

def editMovieInfo():
    clear()
    printMovies()
    editMovie()

def removeMovie():
    #Funcion para eliminar una película del sistema. Muestra las películas disponibles y permite que el usuario seleccione una para eliminar
    clear()
    printMovies()
    

    
    deleteById(EntitiesFields.MOVIES)

    movieId=int(input("Ingrese el ID de la película que desea eliminar:"))
    deleteMovie(movieId)


    

#Funciones para el manejo de las salas---------------------------------------------------------------------------------------------------

#TODO: reutilizar esto como validtion
def cargarHorarios():
    #Funcion que le permite al usuario agregar horiarios disponibles para una sala de cine
    arrayHorarios = []
    patron = r'^([01]\d|2[0-3]):([0-5]\d)$'
    continuar = True

    while continuar:
        horario = input("Agregue un horario en la forma de HH:MM, escriba '-1' para salir: ")
        
        if horario == '-1':
            continuar = False
        elif re.match(patron, horario):
            arrayHorarios.append(horario)
        else:
            print("Formato de horario inválido. Por favor, use HH:MM (ejemplo: 09:30, 14:45).")

    return arrayHorarios

def liberarSala():
    #TODO: una vez se cargo una pelicula: se requiere restablecer la sala
    #@fran9300
    return None


def imprimirSala():
    #TODO: imprime el estado actual de la sala
    #@fpelliStudent
    return None

def crearSala():
    clear()
    addRoom()

def CrearFuncionDePelicula():
    clear()
    addRoomConfiguration()

def consultarSalas():
    clear()
    printRooms()

def ReservarEntradas():
    clear()
    global currentUserId
    addReservation(currentUserId)

def VerMisReservas():
    clear()
    global currentUserId
    checkReservations(currentUserId)

def CheckearReservasSalas():
    clear()
    checkRoom()
    

#Funciones para el manejo de los usuarios------------------------------------------------------------------------------------------------

def AgregarNuevoUsuario():
    #Funcion para registrar a un nuevo usuario en el sistema
    clear()
    addUser()

def editUSerInfo():
    #Funcion para editar usuarios
    clear()
    printUsers()
    editUser()

def removeUser():
    # Funcion para eliminar usuarios
    userId=int(input("Ingrese el ID del usuario que desea eliminar: "))

    return None

def viewUsers():
    #Funcion para imprimir los usuarios
    clear()
    printUsers()

def CheckUsuarioActual():
    clear()
    print(f"User ID: {currentUserId}\n")

#Funciones descuentos--------------------------------------------------------------------------------------------------

def configDescuentoPorTipoDePago(metodo):
    #Función para configurar el descuento aplicado según el tipo de pago seleccionado
    if metodo in descuentos:
        return descuentos[metodo]
    else:
        return 0.0

def imprimirDescuentos():
    #Función que muestra los descuentos
    global descuentos
    clear()
    for key in descuentos:
        print(f"{key}: {descuentos[key]*100}% descuento")
    print()

def clientConfig():
    #TODO: permite modificar los datos del cliente, y su metodo de pago
    return None


#Funciones para el manejo de la compra de entradas-----------------------------------------------------------------------------------------


def pedirMetodoDePago():
    #Función que le solicita al usuario el metodo de pago que quiere utilizar
    
    while True:
        print("Opciones de método de pago:")
        
        
        for numero in METODOS_DE_PAGO:
            metodo = METODOS_DE_PAGO[numero]
            print(numero, metodo)
        
        opcion = input("Ingrese el número del método de pago: ")
        
        if opcion.isdigit():  
            opcion = int(opcion)  
            
            if opcion in METODOS_DE_PAGO:  
                return opcion
            else:
                print("El número ingresado no es válido. Ingrese otro número.")
                
        else:
            print("Debe ingresar un número válido. Por favor, intente de nuevo.")

def aplicarDescuento (total,metodoID):
    #Función para aplicar desucento al total según el metodo de pago seleccionado
    if metodoID==5:
        return total
    else:
        descuento=configDescuentoPorTipoDePago(metodoID)
        valorTotal = total * (1-descuento)
        return valorTotal

def ingresarCuponDescuento(total, codigoDescuento):
    # TODO: if si el codigo es igual a 'DESCUENTO' aplica descuento
    #@fran9300
    return None

def chequeoPago(usuario):
    #TODO: recibe el usuario([]) y
    #TODO: chequea que el cliente tenga saldo disponible para pagar la cantidad de entradas que desea comprar(aplica a todos los tipo de pago)
    # @fran9300
    return None

def imprimirFactura():
     #@fran9300
    #TODO: generacionFactura()
    #TODO: Imprime los detalles de la compra, datos del cliente, y que butacas se reservaron
    return None

def aplicarPuntos(total):
    #Funcion para aplicar los puntos al total de la compra. Resta los puntos al total
    while True:
        puntos = input("Ingrese la cantidad de puntos a utilizar (1 punto = 1 peso, o ingrese 0 para no utilizar puntos): ")
        if puntos.isdigit():
            puntos = int(puntos)
            if puntos <= total:
                totalPoints=total-puntos
                return totalPoints
            else:
                print(f"No puede utilizar más puntos de los que corresponden al total ({total} puntos). Intente de nuevo.")
        else:
            print("Debe ingresar un número válido de puntos. Por favor, intente de nuevo.")

def comprarEntrada():
    #FLUJO DE COMPRAR PELICULA
    #Esto es el flujo pero no esta implementado
    # viewMovies()
    #elegir pelicula
    #elegir horario que tengan butacas disponibles: muestro todos los horarios  o solo los horarios con butacas disponibles
    # Consultar cantida de entradas
    # imprimirSala() # para ver estado actual de la sala
    # elegirButacas()
    # calcularTotal()
    # pedirMetodoDePago()
    # aplicarDescuento()
    # ingresarCuponDescuento()
    #confirmar
    # chequeoPago()
    # reservarButaca()
    # imprimirFactura()
    return None

#Funciones para el manejo del menu interactivo-----------------------------------------------------------------------------------------

def imprimirMenu(menu):
    print("Ingrese el número de alguna de las siguientes opciones o escriba 'exit' para salir: \n")
    for key in menu.keys():
        print(f"{key}-{menu[key].__name__}")

def GestionPeliculas():
    clear()
    global currentMenu    
    currentMenu  = gestionPeliculas

def GestionUsuarios():
    clear()
    global currentMenu
    currentMenu = gestionUsuarios

def LoginMenu():
    clear()
    global currentMenu
    currentMenu = loginMenu

def GestionSalas():
    clear()
    global currentMenu
    currentMenu = gestionSalas


def IniciarSesion():
    global currentMenu,mainMenu, currentUserId
    user = None
    intentos = 0
    intentosMax = 3
    clear()
    while user == None and intentos < intentosMax:
        intentos += 1
        user = input("Ingrese usuario: ")
        password = input("Ingrese contraseña: ")
        user = checkUserAndPass(user,password)
        if user == None:
            print(f"\nIntento fallido {intentos} de {intentosMax}.\n")
    if user == None:
        clear()
        print("\nHa alcanzado el número máximo de intentos. Intente nuevamente más tarde.\n")
        currentMenu = loginMenu
        return 
    clear()
    if user["role"] == 1:
        mainMenu = mainMenuAdmin        
    elif user["role"] == 2:
        mainMenu = mainMenuUser
    currentMenu = mainMenu
    currentUserId = user["id"]

def Registro():
    clear()
    NewUser()

#Programa principal


def volverMenuPrincipal():
    clear()
    global currentMenu
    currentMenu = mainMenu

gestionPeliculas = {
    "1":viewMovies,
    "2":loadMovie,
    "3":removeMovie,
    "4":editMovieInfo,
    "5":volverMenuPrincipal
}

gestionSalas = {
    "1":consultarSalas,
    "2":crearSala,
    "3":CrearFuncionDePelicula,
    "4":liberarSala,
    "5":VerificarPrecioEntrada,
    "6":ModificarValorEntrada,
    "7":CheckearReservasSalas,
    "8":volverMenuPrincipal
}

gestionUsuarios = {
    "1": viewUsers,
    "2": AgregarNuevoUsuario,
    "3": editUSerInfo,
    "4": removeMovie,
    "5": volverMenuPrincipal
}

mainMenuAdmin = {
    "1":GestionPeliculas,
    "2":GestionSalas,
    "3":GestionUsuarios,
    "4":configDescuentoPorTipoDePago,
    "5":imprimirDescuentos,
    "6":CheckUsuarioActual,
    "7":LoginMenu
    
}

mainMenuUser = {
    #TODO agregar opciones para el usuario
    "1":viewMovies,
    "2":CheckearReservasSalas,
    "3":ReservarEntradas,
    "4":VerMisReservas,
    "5":CheckUsuarioActual,
    "6":LoginMenu
    
}

loginMenu = {
    "1":Registro,
    "2":IniciarSesion
}


# print("ejemplo getById")
# print(getById(2,getMovies()))      

# PROBAR :D
# print(getEntityByProperties("USER",["username","name"],"fpelli","Franco")) 
# print(repositories.repository.getEntityById("USER",1))
initDefaultValues()

currentMenu = loginMenu
option = ''
while option != 'exit':
    imprimirMenu(currentMenu)
    print()
    option = input()
    if option != 'exit':
        while not  option in currentMenu.keys() or option == 'exit':
                print("El valor ingresado no existe en el menu, vuelva a ingresar" )
                option = input()
        if option != 'exit':
            currentMenu[option]()
    
