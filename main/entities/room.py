from repositories.repository import addEntity
from entities import entitiesEnum


def addRoom():

    newRoom = {}
    newRoom[entitiesEnum.ROOM_NAME] = input("ingrese nombre de sala")
    newRoom[entitiesEnum.ROOM_ROWS] = input("ingrese cantidad de filas") #agregar validator para no tener fils mas de 30
    newRoom[entitiesEnum.ROOM_NAME] = input("ingrese cantidad de columnas") #idem
    newRoom[entitiesEnum.TYPE] = entitiesEnum.ROOM
    #Las validaciones las podemos hacer con unas lambdas y que se llamen automaticamente desde el add entity, despues vemos
    addEntity(newRoom)

def updateRoom():
    #TODO
    return None
