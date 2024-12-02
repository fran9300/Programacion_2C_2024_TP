import json
from repositories.path import getPath
from entities import EntitiesFields
from entities.utils import getById
from utils.validator import validateEntity
import copy
cachedEntities = {
    EntitiesFields.USER : [],
    EntitiesFields.MOVIES: [],
    EntitiesFields.SECUENCE: [],
    EntitiesFields.ROOM: [],
    EntitiesFields.ROOM_CONFIGURATION: [],
    EntitiesFields.RESERVATION: [],
    EntitiesFields.USER_PAYMENT: []
}

def logicDelete():
    #Se debe permitir eliminar una entidad de manera logica. Evitar borrado fisco.
    #Creo q esto hay q borarrlo
    return None

def convertValues(entity):
    entityType = entity[EntitiesFields.TYPE]
    fields = EntitiesFields.FIELDS[entityType]
    for field in fields:
        if field != EntitiesFields.ID and field != EntitiesFields.DELETED:
            entity[field] = EntitiesFields.convertValue(entity[field],EntitiesFields.FIELDS_TYPES[field])
    return entity


def autoInsertId(entity,type):
    secuences = loadData(EntitiesFields.SECUENCE)
    nextId = secuences[type]
    entity[EntitiesFields.ID] = nextId
    secuences[type] = secuences[type] +1
    saveData(secuences,EntitiesFields.SECUENCE)
    return entity

    

def updateEntity(updatedEntity):
    validateEntity(updatedEntity,True)
    updatedEntity = convertValues(updatedEntity)

    type = ""
    if "type" in updatedEntity:
        type = updatedEntity["type"].upper()
        del updatedEntity["type"]
    entities = loadData(type)
    originalEntity = getById(updatedEntity["id"], entities)
    if originalEntity == -1:
        raise Exception(f"Entidad con ID {updatedEntity['id']} no encontrada para el tipo '{type}'")
    index = entities.index(originalEntity)
    entities[index].update(updatedEntity)
    saveData(entities, type)


def deleteById(entity_type):
    printEntities(entity_type)
    entityId = int(input(f"Ingrese el ID de la {entity_type.lower()} a eliminar: "))
    entityToDelete = getEntityById(entity_type, entityId)

    if not entityToDelete:
        print(f"No se encontró ninguna {entity_type.lower()} con ID:", entityId)
    else:
        entityToDelete[EntitiesFields.DELETED] = True
        entityToDelete[EntitiesFields.TYPE] = entity_type
        updateEntity(entityToDelete)
        print(f"\n{entity_type.capitalize()} con ID {entityId} ha sido eliminada lógicamente del sistema.\n")





def initDefaultFile(value):
#funcion generica, se le pasa el key y se trae el path y los valores default. Ademas comprueba que no exista el archivo para no pisar los datos existentes
    key = value.upper()
    try:
        file = open(getPath(key),"r")
        file.close()
    except FileNotFoundError:
        default = getDefaultValue(key)
        with open(getPath(key),"w") as file:
            json.dump(default,file)

#Valores default
defaultValues = {
    EntitiesFields.USER: [{EntitiesFields.ID:1, EntitiesFields.USER_USERNAME:"admin",EntitiesFields.USER_NAME:"",
                           EntitiesFields.USER_LASTNAME: "", EntitiesFields.USER_PASSWORD:"admin", EntitiesFields.USER_ROLE:1,
                           EntitiesFields.USER_EMAIL:"", EntitiesFields.USER_CREDIT:10000, EntitiesFields.DELETED:False},
                           {EntitiesFields.ID:2, EntitiesFields.USER_USERNAME:"fpelli",EntitiesFields.USER_NAME:"Franco",
                           EntitiesFields.USER_LASTNAME: "Pelli", EntitiesFields.USER_PASSWORD:"contraseña", EntitiesFields.USER_ROLE:2,
                           EntitiesFields.USER_EMAIL:"fpelli@uade.edu.ar", EntitiesFields.USER_CREDIT:10000, EntitiesFields.DELETED:False},
                           {EntitiesFields.ID:3, EntitiesFields.USER_USERNAME:"user",EntitiesFields.USER_NAME:"user",
                           EntitiesFields.USER_LASTNAME: "user", EntitiesFields.USER_PASSWORD:"user", EntitiesFields.USER_ROLE:2,
                           EntitiesFields.USER_EMAIL:"", EntitiesFields.USER_CREDIT:10000, EntitiesFields.DELETED:False}],

    EntitiesFields.MOVIES: [{EntitiesFields.ID:1, EntitiesFields.MOVIE_TITLE:"Deadpool",EntitiesFields.MOVIE_DURATION:127,
                           EntitiesFields.MOVIE_GENRE: "Superheroes", EntitiesFields.MOVIE_CATEGORY:"Accion", EntitiesFields.MOVIE_RATING:"18",
                           EntitiesFields.MOVIE_RELEASEDATE:"20/07/2024", EntitiesFields.DELETED:False},
                           {EntitiesFields.ID:2, EntitiesFields.MOVIE_TITLE:"Longlegs",EntitiesFields.MOVIE_DURATION:"100",
                           EntitiesFields.MOVIE_GENRE: "pelicula de terror", EntitiesFields.MOVIE_CATEGORY:"terror", EntitiesFields.MOVIE_RATING:"13",
                           EntitiesFields.MOVIE_RELEASEDATE:"20/09/2024", EntitiesFields.DELETED:False},
                           {EntitiesFields.ID:3, EntitiesFields.MOVIE_TITLE:"Alien",EntitiesFields.MOVIE_DURATION:"100",
                           EntitiesFields.MOVIE_GENRE: "pelicula de aliens", EntitiesFields.MOVIE_CATEGORY:"suspenso", EntitiesFields.MOVIE_RATING:"18",
                           EntitiesFields.MOVIE_RELEASEDATE:"20/10/2024", EntitiesFields.DELETED:False}],

    EntitiesFields.ROOM:[{EntitiesFields.ID:1,EntitiesFields.ROOM_NAME:"test",EntitiesFields.ROOM_COLUMNS:20,EntitiesFields.ROOM_ROWS:10,EntitiesFields.DELETED:False},
                         {EntitiesFields.ID:2,EntitiesFields.ROOM_NAME:"test2",EntitiesFields.ROOM_COLUMNS:20,EntitiesFields.ROOM_ROWS:10,EntitiesFields.DELETED:False},
                         {EntitiesFields.ID:3,EntitiesFields.ROOM_NAME:"test3",EntitiesFields.ROOM_COLUMNS:20,EntitiesFields.ROOM_ROWS:10,EntitiesFields.DELETED:False}],

    EntitiesFields.ROOM_CONFIGURATION:[{EntitiesFields.ID:1,EntitiesFields.CONFIG_MOVIE_ID: 1,EntitiesFields.CONFIG_ROOM_ID:1,EntitiesFields.CONFIG_DAY:"Lunes",EntitiesFields.CONFIG_TIME:"16:00",EntitiesFields.DELETED:False},
                                       {EntitiesFields.ID:2,EntitiesFields.CONFIG_MOVIE_ID: 2,EntitiesFields.CONFIG_ROOM_ID:2,EntitiesFields.CONFIG_DAY:"Martes",EntitiesFields.CONFIG_TIME:"17:00",EntitiesFields.DELETED:False},
                                       {EntitiesFields.ID:3,EntitiesFields.CONFIG_MOVIE_ID: 3,EntitiesFields.CONFIG_ROOM_ID:3,EntitiesFields.CONFIG_DAY:"Miercoles",EntitiesFields.CONFIG_TIME:"18:00",EntitiesFields.DELETED:False},
                                       {EntitiesFields.ID:4,EntitiesFields.CONFIG_MOVIE_ID: 1,EntitiesFields.CONFIG_ROOM_ID:1,EntitiesFields.CONFIG_DAY:"Jueves",EntitiesFields.CONFIG_TIME:"19:00",EntitiesFields.DELETED:False},
                                       {EntitiesFields.ID:5,EntitiesFields.CONFIG_MOVIE_ID: 2,EntitiesFields.CONFIG_ROOM_ID:2,EntitiesFields.CONFIG_DAY:"Viernes",EntitiesFields.CONFIG_TIME:"21:00",EntitiesFields.DELETED:False},
                                       {EntitiesFields.ID:6,EntitiesFields.CONFIG_MOVIE_ID: 3,EntitiesFields.CONFIG_ROOM_ID:3,EntitiesFields.CONFIG_DAY:"Sabado",EntitiesFields.CONFIG_TIME:"20:00",EntitiesFields.DELETED:False}],

    EntitiesFields.RESERVATION:[{EntitiesFields.ID:1,EntitiesFields.RESERVATION_ROOM_ID:1,EntitiesFields.RESERVATION_USER_ID:1,EntitiesFields.RESERVATION_DAY: "Lunes",EntitiesFields.RESERVATION_TIME : "16:00",EntitiesFields.RESERVATION_ROW:5,EntitiesFields.RESERVATION_COLUMN:8,EntitiesFields.DELETED:False,EntitiesFields.DELETED:False}],       
    
    EntitiesFields.USER_PAYMENT:[{EntitiesFields.ID:1,EntitiesFields.USER_PAYMENT_USER_ID:3,EntitiesFields.USER_PAYMENT_PAYMENT_TYPE:1,EntitiesFields.USER_PAYMENT_BALANCE:10000},
                                 {EntitiesFields.ID:1,EntitiesFields.USER_PAYMENT_USER_ID:3,EntitiesFields.USER_PAYMENT_PAYMENT_TYPE:2,EntitiesFields.USER_PAYMENT_BALANCE:20000},
                                 {EntitiesFields.ID:1,EntitiesFields.USER_PAYMENT_USER_ID:3,EntitiesFields.USER_PAYMENT_PAYMENT_TYPE:3,EntitiesFields.USER_PAYMENT_BALANCE:30000},
                                 {EntitiesFields.ID:1,EntitiesFields.USER_PAYMENT_USER_ID:3,EntitiesFields.USER_PAYMENT_PAYMENT_TYPE:4,EntitiesFields.USER_PAYMENT_BALANCE:40000},
                                 {EntitiesFields.ID:1,EntitiesFields.USER_PAYMENT_USER_ID:3,EntitiesFields.USER_PAYMENT_PAYMENT_TYPE:5,EntitiesFields.USER_PAYMENT_BALANCE:500}],
    
    EntitiesFields.SECUENCE:{"USER" : 4,"MOVIES" : 4,"ROOM" : 4,"ROOM_CONFIGURATION":7,"RESERVATION":4}


}

def initDefaultValues():
    initDefaultFile(EntitiesFields.USER)
    initDefaultFile(EntitiesFields.SECUENCE)
    initDefaultFile(EntitiesFields.MOVIES)
    initDefaultFile(EntitiesFields.ROOM)
    initDefaultFile(EntitiesFields.ROOM_CONFIGURATION)
    initDefaultFile(EntitiesFields.RESERVATION)
    initDefaultFile(EntitiesFields.USER_PAYMENT)

#Try-Catch
def getDefaultValue(value):
    try:
        key = value.upper()
        return defaultValues[key]
    except KeyError:
        print(f"Error: No hay valores por defecto para '{value}'")
        return None

def getEntityByProperties(entityType,properties,*values):
    #función para obtener una entidad usando una propiedad de la misma, se pueden utilizar varias propiedades y valores siempre y cuando sean la misma cantidad
    entities = loadData(entityType)
    quantity = len(properties)
    if (len(properties) != len(values)):
        raise Exception("Cantidad de variables distinta a la cantidad de properties")
    for entity in entities:
        matches = 0
        for i,parameter in enumerate(values):
            if entity[properties[i]] == parameter:
                matches += 1
        if matches == quantity:
            return entity

#Esta funcion es muy util porque nos va a servir para el tema de salas, ya que podemos filtrar entre todas la reservas por un id de sala
def listByProperties(entityType,properties,*values):
    entities = loadData(entityType)
    quantity = len(properties)
    response = []
    if (len(properties) != len(values)):
        raise Exception("Cantidad de variables distinta a la cantidad de properties")
    for entity in entities:
        matches = 0
        for i,parameter in enumerate(values):
            if entity[properties[i]] == parameter:
                matches += 1
        if matches == quantity:
            response.append(entity)
    return response

def getEntityById(entityType,id):
    return copy.deepcopy(getEntityByProperties(entityType,["id"],id)) #Se devuelve una copia del objeto porque sino cuando se modifica como que se pisa el objeto en el archivo y rompe los validators


def loadData(value):
    #función para cargar las entidades guardades de su respectivo archivo json.
    #TODO AGREGAR TRY
    try:
        global cachedEntities
        key = value.upper()
        file = None
        if cachedEntities[key] == []:
            file = open(getPath(key),"r")            
            values = json.load(file)     
            cachedEntities[key] = values
            return values
        else:
            return cachedEntities[key]
    finally:
        if(file != None):
            file.close()
            

def saveData(values,type):
    #función para guardar la nueva entidad en su correspondiente archivo json.
    with open(getPath(type),"wt") as file:
        json.dump(values,file)
        cachedEntities[type] = []


def addEntity(entity):
    #función genérica para agregar una nueva entidad recien creada, tal como una pelicula o un usuario.  
    validateEntity(entity,False)
    entity = convertValues(entity)
    type = ""
    if "type" in entity:
        type = entity["type"].upper()
        del entity["type"]
    autoInsertId(entity,type)

    values = loadData(type)
    values.append(entity)
    saveData(values,type)


def printEntities(entityKey):
    # Cargar datos y campos
    entities = loadData(entityKey)
    fields = EntitiesFields.FIELDS[entityKey]

    # Calcular los anchos máximos para las columnas
    max_lengths = [max(len(str(field)), *(len(str(entity[field])) for entity in entities)) for field in fields]

    # Crear el formato dinámico para las filas
    row_format = " | ".join(f"{{:<{length}}}" for length in max_lengths)

    # Imprimir la cabecera
    print(row_format.format(*fields))
    print("-" * (sum(max_lengths) + 3 * (len(fields) - 1)))

    # Imprimir las entidades
    for entity in entities:
        if not entity[EntitiesFields.DELETED]:
            print(row_format.format(*(str(entity[field]) for field in fields)))

    print()


def printAllEntities(entityKey):
    #función genérica para imprimir los distintos tipos de entidades, INCLUSO si poseen verdadero el campo deleted
    entities = loadData(entityKey)
    fields = EntitiesFields.FIELDS[entityKey]
    headerLine = ""
    for field in fields:
        if not headerLine == "":
                headerLine += ' | '
        headerLine += field 
    print(headerLine)
    for entity in entities:
        line = ""
        for field in fields:
            if not line == "":
                line += ' | '
            line += str(entity[field])
        print(line)
    print()



def printCustomEntities(lista, entityKey):
    try:
        # Asegurarse de trabajar con la lista directamente, no llamar a loadData
        entities = lista  # Ahora trabajamos directamente con la lista pasada
        fields = EntitiesFields.FIELDS[entityKey]

        # Calcular los anchos máximos para las columnas
        max_lengths = [max(len(field), *(len(str(entity[field])) for entity in entities if not entity[EntitiesFields.DELETED])) for field in fields]

        # Crear el formato dinámico para las filas
        row_format = " | ".join(f"{{:<{length}}}" for length in max_lengths)

        # Imprimir la cabecera
        print(row_format.format(*fields))
        print("-" * (sum(max_lengths) + 3 * (len(fields) - 1)))

        # Imprimir las entidades
        for entity in entities:
            if not entity[EntitiesFields.DELETED]:
                print(row_format.format(*(str(entity[field]) for field in fields)))

        print()
    except TypeError:
        print("no existen reservas para el usuario actual\n")
    except Exception as e:
        print(f"error desconocido: {e}")



    '''
#funcion para imprimir entidades anterior

def printEntities(entityKey):
    #función genérica para imprimir los distintos tipos de entidades, mientras que el campo deleted sea falso
    entities = loadData(entityKey)
    fields = EntitiesFields.FIELDS[entityKey]
    headerLine = ""
    for field in fields:
        if not headerLine == "":
                headerLine += ' | '
        headerLine += field 
    print(headerLine)
    for entity in entities:
        if entity[EntitiesFields.DELETED] == False:
            line = ""
            for field in fields:
                if not line == "":
                    line += ' | '
                line += str(entity[field])
            print(line)
    print()
    
    #funcion para imprimir una customEntitie anterior

    def printCustomEntities2(lista,type):
    #función genérica para imprimir una lista generica junto con el tipo de entidad, mientras que el campo deleted sea falso
    entities = lista
    fields = EntitiesFields.FIELDS[type]
    headerLine = ""
    for field in fields:
        if not headerLine == "":
                headerLine += ' | '
        headerLine += field 
    print(headerLine)
    for entity in entities:
        if entity[EntitiesFields.DELETED] == False:
            line = ""
            for field in fields:
                if not line == "":
                    line += ' | '
                line += str(entity[field])
            print(line)
    print()
    
    
    
    '''
