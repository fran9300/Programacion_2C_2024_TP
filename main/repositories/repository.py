import json
from repositories.path import getPath
from entities import entitiesEnum

cachedEntities = {
    entitiesEnum.USER : [],
    entitiesEnum.MOVIES: [],
    entitiesEnum.SECUENCE: [],
    entitiesEnum.ROOM: [],
    entitiesEnum.ROOM_CONFIGURATION: [],
    entitiesEnum.RESERVATION: []
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
    secuences = loadData(entitiesEnum.SECUENCE)
    nextId = secuences[type]
    entity[entitiesEnum.ID] = nextId
    secuences[type] = secuences[type] +1
    saveData(secuences,entitiesEnum.SECUENCE)
    return entity


def updateEntity():
    #debe permitir modificar una entidad y savear el archivo. Tiene que remplazar la entidad. por ejemplo si se cambia el campo duracion de 90 -> 120. 
    # Tiene que aparecer 120 en el archivo. pero no crear un nuevo movie sino que remplazar el existente
    return None

# agrgar a todas las entidades un campo deleted para hacer borrado logico.
# EN las entidades agregar un campo que discrimine que tipo es. Luego se busca el path del archivo correspondiente por el tipo de entidad y se guarda ahi.
#  Esto lo vamos a usar para hcer un metodo generico de creacion de entidad


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


defaultValues = {

    entitiesEnum.USER: [
        {"id":1,"username":"fpelli","name":"Franco","lastName":"Pelli","password":"contraseña","role":2,"email":"fpelli@uade.edu.ar","credit":1000},
        {"id":2,"username":"admin","name":"","lastName":"","password":"admin","role":1,"email":"fpelli@uade.edu.ar","credit":1000}],
    entitiesEnum.MOVIES:[],#Agrega default movies y asi con todas las entidades,
    entitiesEnum.ROOM:[{entitiesEnum.ID:1,entitiesEnum.ROOM_NAME:"test",entitiesEnum.ROOM_COLUMNS:20,entitiesEnum.ROOM_ROWS:10}],
    entitiesEnum.ROOM_CONFIGURATION:[{entitiesEnum.ID:1,entitiesEnum.CONFIG_MOVIE_ID: 5,entitiesEnum.CONFIG_TIME:"16:00",entitiesEnum.CONFIG_ROOM_ID:1}],
    entitiesEnum.RESERVATION:[{entitiesEnum.ID:1,entitiesEnum.RESERVATION_ROOM_ID:1,entitiesEnum.RESERVATION_USER_ID:1,entitiesEnum.RESERVATION_ROW:5,entitiesEnum.RESERVATION_COLUMN:8,entitiesEnum.DELETED:False}],                                 
    entitiesEnum.SECUENCE:{"USER" : 4,"MOVIE" : 4,"ROOM" : 4,"ROOM_CONFIGURATION":4,"RESERVATION":4}
}

def getDefaultValue(value):
    #TODO:AGREGAR TRYCATCH
    key = value.upper()
    return defaultValues[key]

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