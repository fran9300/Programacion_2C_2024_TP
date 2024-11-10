import json
from repositories.path import getPath
from entities import EntitiesFields
from entities.utils import getById


cachedEntities = {
    EntitiesFields.USER : [],
    EntitiesFields.MOVIES: [],
    EntitiesFields.SECUENCE: [],
    EntitiesFields.ROOM: [],
    EntitiesFields.ROOM_CONFIGURATION: [],
    EntitiesFields.RESERVATION: []
}

def loadUsers():
    return None

def loadMovies():
    return None

def loadRooms():
    return None

def loadPaymentMethods():
    return None


def logicDelete():
    #Se debe permitir eliminar una entidad de manera logica. Evitar borrado fisco.
    return None

def createTransaction():
    #@fpelli: se debe crear concepto de transaccionalidad.
    return None

def autoInsertId(entity,type):
    secuences = loadData(EntitiesFields.SECUENCE)
    nextId = secuences[type]
    entity[EntitiesFields.ID] = nextId
    secuences[type] = secuences[type] +1
    saveData(secuences,EntitiesFields.SECUENCE)
    return entity

    

def updateEntity(updatedEntity):
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
    entityId = int(input(f"Ingrese el ID de la {entity_type.lower()} a eliminar: "))
    entityToDelete = getEntityById(entity_type, entityId)

    if not entityToDelete:
        print(f"No se encontró ninguna {entity_type.lower()} con ID:", entityId)
    else:
        entityToDelete[EntitiesFields.DELETED] = True
        updateEntity(entityToDelete)
        print(f"\n{entity_type.capitalize()} con ID {entityId} ha sido eliminada lógicamente del sistema.\n")




#Esta funcion es generica, se le pasa el key y se trae el path y los valores default. Ademas comprueba que no exista el archivo para no pisar los datos existentes
def initDefaultFile(value):
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

    EntitiesFields.USER: [
        {"id":1,"username":"fpelli","name":"Franco","lastName":"Pelli","password":"contraseña","role":2,"email":"fpelli@uade.edu.ar","credit":1000,EntitiesFields.DELETED:False},
        {"id":2,"username":"admin","name":"","lastName":"","password":"admin","role":1,"email":"fpelli@uade.edu.ar","credit":1000,EntitiesFields.DELETED:False}],
    EntitiesFields.MOVIES: [
        {"id": 1, "title": "DeadPool", "duration": 127, "genre": "Superheroes", "category": "Accion", "rating": "18", "release_date": "20/07/2024",EntitiesFields.DELETED:False},
        {"id": 2, "title": "Alien", "duration": 112, "genre": "Pelicula de alien", "category": "Suspenso", "rating": "16", "release_date": "20/09/2024",EntitiesFields.DELETED:False},
        {"id": 3, "title": "Longlegs", "duration": 100, "genre": "pelicula de terror", "category": "Terror", "rating": "13", "release_date": "20/08/2024",EntitiesFields.DELETED:False}],
    EntitiesFields.ROOM:[{EntitiesFields.ID:1,EntitiesFields.ROOM_NAME:"test",EntitiesFields.ROOM_COLUMNS:20,EntitiesFields.ROOM_ROWS:10,EntitiesFields.DELETED:False}],
    EntitiesFields.ROOM_CONFIGURATION:[{EntitiesFields.ID:1,EntitiesFields.CONFIG_MOVIE_ID: 5,EntitiesFields.CONFIG_TIME:"16:00",EntitiesFields.CONFIG_ROOM_ID:1,EntitiesFields.DELETED:False}],
    EntitiesFields.RESERVATION:[{EntitiesFields.ID:1,EntitiesFields.RESERVATION_ROOM_ID:1,EntitiesFields.RESERVATION_USER_ID:1,EntitiesFields.RESERVATION_ROW:5,EntitiesFields.RESERVATION_COLUMN:8,EntitiesFields.DELETED:False,EntitiesFields.DELETED:False}],                                 
    EntitiesFields.SECUENCE:{"USER" : 4,"MOVIE" : 4,"ROOM" : 4,"ROOM_CONFIGURATION":4,"RESERVATION":4}


}

def initDefaultValues():
    initDefaultFile(EntitiesFields.USER)
    initDefaultFile(EntitiesFields.SECUENCE)
    #TODO:agregar el de movie
    initDefaultFile(EntitiesFields.ROOM)
    initDefaultFile(EntitiesFields.ROOM_CONFIGURATION)
    initDefaultFile(EntitiesFields.RESERVATION)

#Try-Catch
def getDefaultValue(value):
    try:
        key = value.upper()
        return defaultValues[key]
    except KeyError:
        print(f"Error: No hay valores por defecto para '{value}'")
        return None

def getEntityByProperties(entityType,properties,*values):
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
    return getEntityByProperties(entityType,["id"],id)


def loadData(value):
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
    with open(getPath(type),"wt") as file:
        json.dump(values,file)
        cachedEntities[type] = []


def addEntity(entity): 
    type = ""
    if "type" in entity:
        type = entity["type"].upper()
        del entity["type"]
    autoInsertId(entity,type)
    values = loadData(type)
    values.append(entity)
    saveData(values,type)

def printEntities(entityKey):
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



