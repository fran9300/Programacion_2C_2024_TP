from entities import EntitiesFields
from repositories.repository import getEntityByProperties,addEntity,listByProperties

def addReservation(entity):
    #TODO: HACER ACA EL FORMULARIO de reserva, no debe recibir parametro
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
    return True if found else False