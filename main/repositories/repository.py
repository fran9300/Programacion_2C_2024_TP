import json
from repositories.path import getPath


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

def autoInsertId(entidad):
    #@aMieres: se debe crear una funcion que cuando le llegue una entidad, busque la secuencia y obtenga su valor, se lo asigne a la entidad y devuelva la entidad
    
    return entidad


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
    "USER": [
        {"id":1,"username":"fpelli","name":"Franco","lastName":"Pelli","password":"contraseña","role":2,"email":"fpelli@uade.edu.ar","credit":1000},
        {"id":2,"username":"admin","name":"","lastName":"","password":"admin","role":1,"email":"fpelli@uade.edu.ar","credit":1000}],
    "MOVIE":[]#Agrega default movies y asi con todas las entidades
}

def getDefaultValue(value):
    #TODO:AGREGAR TRYCATCH
    key = value.upper()
    return defaultValues[key]



def loadData(value):
    #TODO AGREGAR TRY
    try:
        key = value.upper()
        file = open(getPath(key),"r")
        values = json.load(file)        
        return values
    finally:
        file.close()

def addEntity(entity):
    type = ""
    if "type" in entity:
        type = entity["type"].upper()
        del entity["type"]
    values = []
    with open(getPath(type),"r") as file:
        values = json.load(file)
    with open(getPath(type),"wt") as file:    
        values.append(entity)
        json.dump(values,file)