
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
    deleteMovie()

#Funciones para el manejo de las salas---------------------------------------------------------------------------------------------------

def liberarSala():
    freeRooms()
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




#Funciones para le manejo de los pagos-------------------------------------------------------------------------------------------------

def cargarSaldoUsuario():
    """Función para cargar saldo para el usuario actual."""
    cargarSaldo(currentUserId)

def listarSaldosUsuario():
    """Función para listar saldos del usuario actual."""
    clear()
    listarSaldos(currentUserId)

def ConfigurarDescuentos(currentUserId):
    configurarDescuentos(currentUserId)




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

def GestionSalas():
    #para ir al menu de manejo de salas
    clear()
    global currentMenu
    currentMenu = gestionSalas

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

def Exit():
    #funcion para salir del programa a travez del menu
    global option
    clear()
    print("Saliendo del programa..")
    option = "exit"


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



#Programa principal------------------------------------------------------------


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
    "4": ConfigurarDescuentos,
    "5": imprimirDescuentos,
    "6": LoginMenu,
    "7": Exit,
    
}

mainMenuUser = {
    "1": viewMovies,
    "2": CheckearReservasSalas,
    "3": ReservarEntradas,
    "4": VerMisReservas,
    "5": ConfigurarUsuario,
    "6": LoginMenu,
    "7": Exit,
}

loginMenu = {
    "1":Registro,
    "2":IniciarSesion,
    "3": Exit,
}



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
    
