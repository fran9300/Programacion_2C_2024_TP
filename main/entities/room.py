from repositories.repository import addEntity, updateEntity, getEntityById, loadData, deleteById, listByProperties, printEntities
from entities import EntitiesFields

#ABM salas
def addRoom():
    try:
        newRoom = {
                    "type": "ROOM",
                    EntitiesFields.ROOM_FIELDS[1]: input("ingrese nombre de sala: "),
                    EntitiesFields.ROOM_FIELDS[2]: int(input("ingrese cantidad de filas: ")),#agregar validator para no tener fils mas de 30
                    EntitiesFields.ROOM_FIELDS[3]: int(input("ingrese cantidad de columnas: ")),#idem
                    EntitiesFields.DELETED : False
        }
        confirmacion = int(input("\npresione 1 para confirmar, 0 para cancelar: "))
    except ValueError:
        print("\nintroduzca valores numéricos enteros para las filas y columnas\n")
    #Las validaciones las podemos hacer con unas lambdas y que se llamen automaticamente desde el add entity, despues vemos
    else:
        if confirmacion == 1:
            addEntity(newRoom)
            print("\nNueva sala agregada al sistema.\n")
        else:
            print("\noperacion cancelada\n")


def editRoom():
    roomId = int(input("Ingrese el ID de la sala a editar: "))
    roomToEdit = getEntityById(EntitiesFields.ROOM, roomId)

    if not roomToEdit:
        print("No se encontró ninguna sala con ID:", roomId)
    else:
        editing = True
        while editing:
            print("\nEditando la sala:", roomToEdit)
            print("Seleccione el campo que desea editar:")
            print("1. Nombre")
            print("2. Cantidad de filas")
            print("3. Cantidad de columnas")
            print("4. Terminar de editar\n")

            choice = int(input("Elige una opción: "))
            if choice == 4:
                editing = False
                print("\nEdición finalizada.")
            elif choice == 1:
                roomToEdit[EntitiesFields.ROOM_NAME] = input("Ingrese el nuevo nombre de la sala: ")
            elif choice == 2:
                filas = int(input("Ingrese la nueva cantidad de filas (máximo 30): "))
                if 1 <= filas <= 30:
                    roomToEdit[EntitiesFields.ROOM_ROWS] = filas
                else:
                    print("Error: La cantidad de filas debe estar entre 1 y 30.")
            elif choice == 3:
                columnas = int(input("Ingrese la nueva cantidad de columnas (máximo 30): "))
                if 1 <= columnas <= 30:
                    roomToEdit[EntitiesFields.ROOM_COLUMNS] = columnas
                else:
                    print("Error: La cantidad de columnas debe estar entre 1 y 30.")
            else:
                print("Opción no válida.")

        
        updateEntity(roomToEdit)
        print("\nSala con ID", roomId, "ha sido actualizada en el sistema.\n")

def deleteRoom():    
    deleteById(EntitiesFields.ROOM)


def printRooms():
    printEntities(EntitiesFields.ROOM)



#Funcion para liberar sala
def freeRooms():
    
    print("Salas disponibles:")
    printRooms()  
    try:
        room_id = int(input("Ingrese el ID de la sala que desea liberar: "))
    except ValueError:
        print("ID de sala inválido. Por favor, ingrese un número.")
        return

    sala = getEntityById(EntitiesFields.ROOM, room_id)
    if not sala:
        print("No se encontró ninguna sala con el ID especificado.")
        return
    
    # Obtener todas las reservas activas de la sala seleccionada
    reservas = listByProperties(EntitiesFields.RESERVATION, [EntitiesFields.RESERVATION_ROOM_ID, EntitiesFields.DELETED], room_id, False)
    
    if not reservas:
        print(f"La sala con ID {room_id} no tiene reservas activas.")
        return

    # Eliminar (liberar) cada reserva de la sala
    for reserva in reservas:
        reserva[EntitiesFields.DELETED] = True  # Marcar la reserva como eliminada
        updateEntity(reserva)  # Guardar el cambio en la reserva

    print(f"Todas las reservas de la sala con ID {room_id} han sido liberadas.")

def updateRoom():
    #TODO
    return None
