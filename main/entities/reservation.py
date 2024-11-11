from entities import EntitiesFields
from repositories.repository import getEntityByProperties,addEntity,listByProperties
from entities.movies import printMovies

def addReservation(userId):
    printMovies()
    print()
    id_reserva = int(input("seleccion el id de la pelicula a reservar: "))
    sala_reserva = getEntityByProperties(EntitiesFields.ROOM_CONFIGURATION,[EntitiesFields.CONFIG_MOVIE_ID],id_reserva)
    print(sala_reserva["id"])
    showRoom(sala_reserva["id"])
    cantidad_entradas = int(input("indique la cantidad de entradas que desea reservar o 0 para cancelar la reserva: "))
    i = 0

    while i != cantidad_entradas: 
        fila_aciento_reserva = int(input("seleccione fila del aciento deseado: "))
        columna_aciento_reserva = int(input("seleccione columna del aciento deseado: "))
        
        if checkAvailable(sala_reserva["roomId"],fila_aciento_reserva,columna_aciento_reserva):
                newReservation = {
                        "type": "RESERVATION",
                        EntitiesFields.RESERVATION_FIELDS[1]: sala_reserva["roomId"],
                        EntitiesFields.RESERVATION_FIELDS[2]: userId,
                        EntitiesFields.RESERVATION_FIELDS[3]: fila_aciento_reserva,
                        EntitiesFields.RESERVATION_FIELDS[4]: columna_aciento_reserva,
                        EntitiesFields.DELETED : False
                        }
                addEntity(newReservation)
                print("\nNueva reserva guardada.\n")
                i += 1
        else:
            print("\naciento ya reservado, por favor seleccione otro.\n")

    if cantidad_entradas != 0:
        importe = cantidad_entradas * 5000
        print(f"\nReserva del usuario numero: {userId}")
        print(f"importe total de :{importe} pesos\n")


def showRoom(roomConfigId):
    roomConfig = getEntityByProperties(EntitiesFields.ROOM_CONFIGURATION,[EntitiesFields.ID],roomConfigId)
    room = getEntityByProperties(EntitiesFields.ROOM,[EntitiesFields.ID],roomConfig[EntitiesFields.CONFIG_ROOM_ID])
    values = listByProperties(EntitiesFields.RESERVATION,[EntitiesFields.RESERVATION_ROOM_ID,EntitiesFields.DELETED],roomConfigId,False)
    arr =[[0 for _ in range(room[EntitiesFields.ROOM_COLUMNS])] for _ in range(room[EntitiesFields.ROOM_ROWS])] ## esto deberia setearse segun lo onfigurado en la sala
    
    for value in values:
        arr[value[EntitiesFields.RESERVATION_ROW]-1][value[EntitiesFields.RESERVATION_COLUMN]-1] = 1
    for column in arr:
        row = ''
        for i in column:
            row += '⬛' if i == 0 else '🟥'
        print("--------------------------------")
        print(row)



def checkAvailable(roomId,row,column):
    found = getEntityByProperties(EntitiesFields.RESERVATION,[EntitiesFields.RESERVATION_ROOM_ID,EntitiesFields.RESERVATION_ROW,EntitiesFields.RESERVATION_COLUMN,EntitiesFields.DELETED],roomId,row,column,False)
    return False if found else True




    #TODO: HACER ACA EL FORMULARIO de reserva, no debe recibir parametro
    '''
    entity.keys()
    if EntitiesFields.RESERVATION_USER_ID not in entity.keys():
        #tirar exception
        True == True
    if EntitiesFields.RESERVATION_ROOM_ID not in entity.keys():
        True == True
        #tirar exception
    #agregar validacion de que la columna y fila este dentro de lo configurado en la sala
    row = entity[EntitiesFields.RESERVATION_ROW]
    column = entity[EntitiesFields.RESERVATION_COLUMN]
    roomId = entity[EntitiesFields.RESERVATION_ROOM_ID]
    if(checkAvailable(roomId,row, column)):
        addEntity(entity)
    '''