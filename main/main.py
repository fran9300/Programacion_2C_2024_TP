
from entities.movies import addMovie,printMovies,deleteMovie,editMovie
from entities.user import getUsers, addUser, editUser, deleteUser,printUsers, checkUserAndPass
from entities.reservation import addReservation, checkReservations, checkRoom
from entities.utils import clear
from entities.room import addRoom, printRooms, deleteRoom,freeRooms
from entities.room_configuration import addRoomConfiguration,printConfigRoom,deleteConfigRoom
import os
import re
from repositories.repository import getEntityByProperties,initDefaultValues,printEntities, deleteById, EntitiesFields
from utils.translator import getTranslation
from entities.user_payment import cargarSaldo, listarSaldos, elegirMetodoPago
from entities.payment_methods import cargarDescuentos, imprimirDescuentos, guardarDescuentos, configurarDescuentos
from entities.ticket_value import * 

#Arrays y variables con datos hardcodeados ----------------------------------------------------------------------------------------

currentMenu = {}
mainMenu = {}
currentUserId = ""



#-----------------------------------------------------------------------------------------------------------------------------------------

# def VerificarPrecioEntrada():
#     #muestra el precio de la entrada estandar de cine
    
#     clear()
#     print(f"\nvalor actual de la entrada de cine: {valorEntrada}\n")

# def ModificarValorEntrada():
#     #TODO cambiar a entidad para poder guardarla en un archivo json
#     #modificar el valor de la entrada estandar, es solo momentaneo y mas tarde va a ser modificado
#     global valorEntrada
#     VerificarPrecioEntrada()
#     try:
#         valorEntrada = float(input("ingrese el valor de la entrada estandar de cine: "))
#         confirmacion = int(input("\npresione 1 para confirmar, 0 para cancelar: "))
#     except ValueError:
#         clear()
#         print("valor incorrecto, ingrese un numero con . para el precio de la entrada\n")
#     else:
#         clear()
#         if confirmacion == 1:
#             print("\rprecio de la entrada actualizado correctamente\n")
#         else:
#             print("\noperacion cancelada\n")

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
    freeRooms()
    return None


def imprimirSala():
    #TODO: imprime el estado actual de la sala
    #@fpelliStudent
    return None

def crearSala():
    clear()
    addRoom()

def eliminarSala():
    clear()
    deleteRoom()

def CrearFuncionDePelicula():
    clear()
    addRoomConfiguration()

def MostrarFuncionesProgramadas():
    clear()
    printConfigRoom()
def EliminarFuncionProgramada():
    clear()
    deleteConfigRoom()

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
    editUser()

def eliminarUsuario():
    deleteUser()

def viewUsers():
    #Funcion para imprimir los usuarios
    clear()
    printUsers()



"""
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
"""
#Funciones para el manejo de la compra de entradas-----------------------------------------------------------------------------------------

"""
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

    """
#Funciones para el manejo del menu interactivo-----------------------------------------------------------------------------------------

def imprimirMenu(menu):
    #función para imprimir el menu actual
    print("Ingrese el número de alguna de las siguientes opciones o escriba 'exit' para salir: \n")
    for key in menu.keys():
        itemName = getTranslation(menu[key].__name__)
        print(f"{key}-{itemName}")

def ConfigurarUsuario():
    #para ir al menu de gestion de películas
    clear()
    global currentMenu    
    currentMenu  = configurarUsuario

def GestionPeliculas():
    #para ir al menu de gestion de películas
    clear()
    global currentMenu    
    currentMenu  = gestionPeliculas

def GestionUsuarios():
    #para ir al menu de manejo de usuarios
    clear()
    global currentMenu
    currentMenu = gestionUsuarios

def LoginMenu():
    #para ir al menu de logeo
    clear()
    global currentMenu
    currentMenu = loginMenu

def GestionSalas():
    #para ir al menu de manejo de salas
    clear()
    global currentMenu
    currentMenu = gestionSalas


def IniciarSesion():
    #función de inicio de sesión
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
    if user[EntitiesFields.USER_ROLE] == 1:
        mainMenu = mainMenuAdmin        
    elif user[EntitiesFields.USER_ROLE] == 2:
        mainMenu = mainMenuUser
    currentMenu = mainMenu
    currentUserId = user[EntitiesFields.ID]

def Registro():
    clear()
    addUser()



# Definir funciones descriptivas para el menú
def cargarSaldoUsuario():
    """Función para cargar saldo para el usuario actual."""
    cargarSaldo(currentUserId)

def listarSaldosUsuario():
    """Función para listar saldos del usuario actual."""
    listarSaldos(currentUserId)


#Programa principal


def volverMenuPrincipal():
    #permite volver al mainMenu, por ahora no estamos utilizando mas andiameinto de menues.
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
    "3":eliminarSala,
    "4":CrearFuncionDePelicula,
    "5":MostrarFuncionesProgramadas,
    "6":EliminarFuncionProgramada,
    "7":liberarSala,
    "8":checkTicketValue,
    "9":updateTicketValue,
    "10":CheckearReservasSalas,
    "11":volverMenuPrincipal
}

gestionUsuarios = {
    "1": viewUsers,
    "2": AgregarNuevoUsuario,
    "3": editUSerInfo,
    "4": eliminarUsuario,
    "5": volverMenuPrincipal
}

configurarUsuario = {
    "1": cargarSaldoUsuario,
    "2": listarSaldosUsuario,
    "3": volverMenuPrincipal
}

mainMenuAdmin = {
    "1": GestionPeliculas,
    "2": GestionSalas,
    "3": GestionUsuarios,
    "4": configurarDescuentos,  # Configurar descuentos
    "5": imprimirDescuentos,
    "6": LoginMenu
    
}

mainMenuUser = {
    "1": viewMovies,
    "2": CheckearReservasSalas,
    "3": ReservarEntradas,
    "4": VerMisReservas,
    "5": ConfigurarUsuario,
    "6": LoginMenu
    
}

loginMenu = {
    "1":Registro,
    "2":IniciarSesion,
}


# print("ejemplo getById")
# print(getById(2,getMovies()))      

# PROBAR :D
# print(getEntityByProperties("USER",["username","name"],"fpelli","Franco")) 
# print(repositories.repository.getEntityById("USER",1))
initDefaultValues()




currentMenu = loginMenu
option = ''
clear()
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
    
