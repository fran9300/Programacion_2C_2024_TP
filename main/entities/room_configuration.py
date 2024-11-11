import entities.EntitiesFields as EntitiesFields
from repositories.repository import addEntity, printEntities
from entities.utils import clear


def addRoomConfiguration():

    clear()
    print("salas disponibles:")
    printEntities("ROOM")
    print()
    print("películas disponibles:")
    printEntities("MOVIES")
    print()

    newConfig = {"type": "ROOM_CONFIGURATION",
                EntitiesFields.CONFIG_FIELDS[1]: int(input("ingrese el id de la pelicula")),
                EntitiesFields.CONFIG_FIELDS[2]: int(input("ingrese el id de la sala")),
                EntitiesFields.CONFIG_FIELDS[3]: input("Ingrese día de la funcion"),
                EntitiesFields.CONFIG_FIELDS[4]: input("Ingrese horario de la funcion"),
                EntitiesFields.DELETED : False,
                 }
    addEntity(newConfig)
    print("\nNueva funcion de pelicula agregada al sistema.\n")


def updateRoomConfiguration(id):
    # TODO
    return None