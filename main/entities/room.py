from repositories.repository import addEntity
from main.entities import EntitiesFields


def addRoom():

    newRoom = {}
    newRoom[EntitiesFields.ROOM_NAME] = input("ingrese nombre de sala")
    newRoom[EntitiesFields.ROOM_ROWS] = input("ingrese cantidad de filas") #agregar validator para no tener fils mas de 30
    newRoom[EntitiesFields.ROOM_NAME] = input("ingrese cantidad de columnas") #idem
    newRoom[EntitiesFields.TYPE] = EntitiesFields.ROOM
    #Las validaciones las podemos hacer con unas lambdas y que se llamen automaticamente desde el add entity, despues vemos
    addEntity(newRoom)

def updateRoom():
    #TODO
    return None
