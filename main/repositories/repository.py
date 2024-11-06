import json
from repositories.path import getPath
from entities import entitiesEnum

cachedEntities = {
    entitiesEnum.USER : [],
    entitiesEnum.MOVIES: [],
    entitiesEnum.SECUENCE: []
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

    

def updateEntity(updatedEntity): #Funcion para editar
    type = ""
    if "type" in updatedEntity:
        type = updatedEntity["type"].upper()
        del updatedEntity["type"]
    entities = loadData(type)
    found = False
    for i, entity in enumerate(entities):
        if entity["id"] == updatedEntity["id"]:
            
            entity.update(updatedEntity)
            found = True  
    if not found:
        raise Exception(f"Entidad con ID {updatedEntity['id']} no encontrada para el tipo '{type}'")
    saveData(entities, type)




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

    entitiesEnum.USER: [
        {"id":1,"username":"fpelli","name":"Franco","lastName":"Pelli","password":"contraseña","role":2,"email":"fpelli@uade.edu.ar","credit":1000},
        {"id":2,"username":"admin","name":"","lastName":"","password":"admin","role":1,"email":"fpelli@uade.edu.ar","credit":1000}],
        entitiesEnum.MOVIES: [
        {"id": 1, "title": "DeadPool", "duration": 127, "genre": "Superheroes", "category": "Accion", "rating": "18", "release_date": "20/07/2024"},
        {"id": 2, "title": "Alien", "duration": 112, "genre": "Pelicula de alien", "category": "Suspenso", "rating": "16", "release_date": "20/09/2024"},
        {"id": 3, "title": "Longlegs", "duration": 100, "genre": "pelicula de terror", "category": "Terror", "rating": "13", "release_date": "20/08/2024"}],
   
    entitiesEnum.SECUENCE:{"USER" : 4,"MOVIE" : 4,"ROOM" : 4}
}

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


def addEntity(entity): #Hacer el edit parecido a esta funcion
    type = ""
    if "type" in entity:
        type = entity["type"].upper()
        del entity["type"]
    autoInsertId(entity,type)
    values = loadData(type)
    values.append(entity)
    saveData(values,type)


