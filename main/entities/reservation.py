from entities import entitiesEnum
from repositories.repository import getEntityByProperties,addEntity,listByProperties

def addReservation(entity):
    entity.keys()
    if entitiesEnum.RESERVATION_USER_ID not in entity.keys():
        #tirar exception
        True == True
    if entitiesEnum.RESERVATION_ROOM_ID not in entity.keys():
        True == True
        #tirar exception
    #agregar validacion de que la columna y fila este dentro de lo configurado en la sala
    row = entity[entitiesEnum.RESERVATION_ROW]
    column = entity[entitiesEnum.RESERVATION_COLUMN]
    roomId = entity[entitiesEnum.RESERVATION_ROOM_ID]
    if(checkAvailable(roomId,row, column)):
        addEntity(entity)


def showRoom(roomId):
    values = listByProperties(entitiesEnum.RESERVATION,[entitiesEnum.RESERVATION_ROOM_ID,entitiesEnum.DELETED],roomId,False)
    arr =[[0 for _ in range(24)] for _ in range(10)] ## esto deberia setearse segun lo onfigurado en la sala
    for value in values:
        arr[value[entitiesEnum.RESERVATION_ROW]][value[entitiesEnum.RESERVATION_COLUMN]] = 1
    for column in arr:
        row = ''
        for i in column:
            row += '|O|' if i == 0 else '|x|'
        print("--------------------------------------------------------------------------")
        print(row)



def checkAvailable(roomId,row,column):
    found = getEntityByProperties(entitiesEnum.RESERVATION,[entitiesEnum.RESERVATION_ROOM_ID,entitiesEnum.RESERVATION_ROW,entitiesEnum.RESERVATION_COLUMN,entitiesEnum.DELETED],roomId,row,column,False)
    return True if found else False