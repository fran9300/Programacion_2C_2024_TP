import entitiesEnum
from repositories.repository import addEntity


def addRoomConfiguration():
    config = {}
    #llamar a show rooms asi elige el id
    config[entitiesEnum.CONFIG_ROOM_ID] = input("ingrese el id de la sala") # aca deberiamos hacer una comprobacion de q elige una sala q existe
    config[entitiesEnum.CONFIG_ROOM_TIME] = input("Ingrese horarios")
    #llamar a show movies asi elige el id
    config[entitiesEnum.CONFIG_MOVIE] = input("ingrese el id de la pelicula")
    config[entitiesEnum.TYPE] = entitiesEnum.ROOM_CONFIGURATION
    addEntity(config)


def updateRoomConfiguration(id):
    # TODO
    return None