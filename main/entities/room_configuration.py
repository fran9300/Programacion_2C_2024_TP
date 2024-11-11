import entities.EntitiesFields as EntitiesFields
from repositories.repository import addEntity, printEntities,deleteById
from entities.utils import clear


def addRoomConfiguration():
    #funcion para agregar una nueva salas configuradas, con su pelicula, sala y fecha.
    try:
        clear()
        print("salas disponibles:")
        printEntities(EntitiesFields.ROOM)
        print()
        print("películas disponibles:")
        printEntities(EntitiesFields.MOVIES)
        print()

        newConfig = {"type": EntitiesFields.ROOM_CONFIGURATION,
                    EntitiesFields.ID: int(input("ingrese el id de la pelicula")),
                    EntitiesFields.CONFIG_ROOM_ID: int(input("ingrese el id de la sala")),
                    EntitiesFields.CONFIG_DAY: input("Ingrese día de la funcion"),
                    EntitiesFields.CONFIG_TIME: input("Ingrese horario de la funcion"),
                    EntitiesFields.DELETED : False,
                    }
        addEntity(newConfig)
        print("\nNueva funcion de pelicula agregada al sistema.\n")
    except ValueError:
        print("valor mal introducido, por favor ingrese los mismos segun lo indicado en pantalla\n")


def updateRoomConfiguration(id):
    # TODO
    return None


def printConfigRoom():
    #permite imprimir salas configuradas existentes, utilizando la funcion genérica printEntities
    printEntities(EntitiesFields.ROOM_CONFIGURATION)


def deleteConfigRoom():
    #permite borrar salas configuradas existentes, utilizando la funcion genérica deleteById
    deleteById(EntitiesFields.ROOM_CONFIGURATION)