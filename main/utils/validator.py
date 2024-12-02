from entities.EntitiesFields import *
from utils.translator import getTranslation
import re


currentEntityId = -1
editingGlobal = False

def validateEntity(entity,editing):
    global currentEntityId,editingGlobal
    editingGlobal = editing
    if editing:
        currentEntityId = entity[ID]    
    fields = FIELDS[entity[TYPE]]
    for field in fields:
        validateField(field,entity)
    currentEntityId = -1
    editingGlobal = False

def validateField(field,entity):
    try:
        validations = allValidations[field]
        message = ''
        for validation in validations:
            exception = validation(entity[field])
            if(exception != None):
                message += exception               
        if message != '':
            fieldTraslation = getTranslation(field)
            print(f"El campo \"{fieldTraslation}\" contiene errores:\n {message}")
            newInput = input("Vuelva a ingresar el campo: ")
            entity[field] = newInput
            validateField(field,entity)
    except KeyError:
        return 1


def required(value):
    if(value == None or value == ''):
        return "* El campo es obligatorio\n "
    return ''

def numericString(value):
    if value != None or value != '':
        if not value.isNumeric():
            return "* El campo debe ser un numero\n "
        if int(value) < 0:
            return "* El campo debe ser mayor o igual a 0\n "

def positiveInteger(value):
    try:
        iValue= int(value)
        if iValue < 0:
            return "* El campo debe ser positivo\n "
    except:
        return "* El campo debe ser numerico"

def positiveFloat(value):
    try:
        fValue = float(value)
        if fValue < 0:
            return "* El campo debe ser positivo\n "
    except:
        return "* El campo debe ser numerico\n "

def email(value):    
    regex = r'^\S+@\S+\.\S+$'
    if not bool(re.match(regex, value)):
        return "* Ingresar un formato valido de email\n"

def uniqueUsername(value):
    global editingGlobal
    from repositories.repository import getEntityByProperties
    user = getEntityByProperties(USER,[USER_USERNAME],value)
    if user != None:
        if editingGlobal and user[ID] != currentEntityId:
            return "* El nombre de usuario ingresado no esta disponible\n"
        elif not editingGlobal:
            return "* El nombre de usuario ingresado no esta disponible\n"
        


def uniqueMovieTitle(value):
    global editingGlobal
    from repositories.repository import getEntityByProperties
    movie = getEntityByProperties(MOVIES,[MOVIE_TITLE],value)
    if movie != None:
        if editingGlobal and movie[ID] != currentEntityId:
            return "* El nombre de pelicula ingresado no esta disponible\n"
        elif not editingGlobal:
            return "* El nombre de pelicula ingresado no esta disponible\n"

def dateFormat(value):
    regex = r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$"
    if not bool(re.match(regex, value)):
        return "* La fecha ingresada no cumple el formato dd/mm/aaaa\n"

def timeFormat(value):
    regex="^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$"
    if not bool(re.match(regex, value)):
        return "* La hora ingresada no cumple el formato HH:MM\n"

def passwordStrong(value):
    regex = r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]+$'
    if not  bool(re.match(regex,value)):
        return "* La contraseña debe tener al menos una letra y un caracter\n"
    
def maxValue30(value, max_value=30):
        if int(value) > max_value:
            return f"* El valor no puede ser mayor que {max_value}\n"
        return ''



#Como key se agrega el campo a validar y como valor se agrega un array de validators
allValidations = {
    USER_USERNAME:[required,uniqueUsername],
    USER_EMAIL:[required,email],
    USER_PASSWORD:[required,passwordStrong],

    MOVIE_RELEASEDATE:[required,dateFormat],
    MOVIE_TITLE:[required,uniqueMovieTitle],
    MOVIE_RATING:[required,positiveFloat],
    MOVIE_DURATION:[required,positiveInteger],
    MOVIE_RATING:[required,positiveInteger],

    INVOICE_AMOUNT:[required,positiveFloat],

    USER_PAYMENT_BALANCE:[required,positiveFloat],

    CONFIG_ROOM_ID:[required],
    CONFIG_DAY:[required,dateFormat],
    CONFIG_MOVIE_ID:[required],
    CONFIG_TIME:[required,timeFormat],

    TICKET_VALUE_VALUE:[required,positiveFloat],

    ROOM_NAME:[required],
    ROOM_ROWS: [required,positiveInteger,maxValue30],
    ROOM_COLUMNS: [required,positiveInteger,maxValue30],

}