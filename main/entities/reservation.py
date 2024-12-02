from entities import EntitiesFields
from repositories.repository import getEntityByProperties,addEntity,listByProperties, printCustomEntities,printEntities
from entities.movies import printMovies
from entities.utils import clear
from entities.user_payment import pagarConSaldo

valorEntrada = 5000

def addReservation(userId):
    #permite agregar una nueva reservacion de butacas por parte del usuario. 
    try:
        butacas = []
        printMovies()
        print()
        id_reserva = int(input("seleccion el id de la pelicula a reservar: "))
        
        listaHorarios =(listByProperties(EntitiesFields.ROOM_CONFIGURATION,[EntitiesFields.CONFIG_MOVIE_ID],id_reserva))
        printCustomEntities(listaHorarios,"ROOM_CONFIGURATION")
        
        id_Fecha_Horario = int(input("seleccion el id de la fecha y horario a reservar: "))
        sala_reserva = getEntityByProperties(EntitiesFields.ROOM_CONFIGURATION,[EntitiesFields.ID],id_Fecha_Horario)
        pelicula = getEntityByProperties(EntitiesFields.MOVIES,[EntitiesFields.ID],sala_reserva["movieId"])

        clear()
        print(f"\n{pelicula[EntitiesFields.MOVIE_TITLE]} el día {sala_reserva[EntitiesFields.CONFIG_DAY]} a las {sala_reserva[EntitiesFields.CONFIG_TIME]} hs\n")
        showRoom(sala_reserva["id"])
        cantidad_entradas = int(input("indique la cantidad de entradas que desea reservar (maximo de 6) o 0 para cancelar la reserva: "))

        i = 0

        while i != cantidad_entradas and i != 6 : 
            fila_aciento_reserva = int(input("seleccione fila del asiento deseado: "))
            columna_aciento_reserva = int(input("seleccione columna del asiento deseado: "))
            
            if checkAvailable(sala_reserva["id"],fila_aciento_reserva,columna_aciento_reserva,butacas) and checkBounds(sala_reserva["id"],fila_aciento_reserva,columna_aciento_reserva) :
                    newReservation = {
                            "type": EntitiesFields.RESERVATION,
                            EntitiesFields.RESERVATION_FIELDS[1]: sala_reserva["id"],
                            EntitiesFields.RESERVATION_FIELDS[2]: userId,
                            EntitiesFields.RESERVATION_FIELDS[3]: sala_reserva["day"],
                            EntitiesFields.RESERVATION_FIELDS[4]: sala_reserva["time"],
                            EntitiesFields.RESERVATION_FIELDS[5]: fila_aciento_reserva,
                            EntitiesFields.RESERVATION_FIELDS[6]: columna_aciento_reserva,
                            EntitiesFields.DELETED : False
                            }
                    #addEntity(newReservation)
                    butacas.append(newReservation)
                    clear()
                    print("\nNueva reserva guardada.\n")
                    showRoom(sala_reserva["id"],butacas)
                    i += 1
            else:
                print("\nasiento ya reservado o fuera del rango, por favor seleccione otro.\n")
            

        if cantidad_entradas != 0:
            if cantidad_entradas > 6:
                cantidad_entradas = 6
            importe = cantidad_entradas * valorEntrada
            pago = pagarConSaldo(userId,importe)
            print(pago)
            if pago == True:    
                for butaca in butacas:
                    addEntity(butaca)
                print(f"\nReserva del usuario numero: {userId}")
                print(f"importe total de :{importe} pesos\n")
        else:
            clear()
            print("operación cancelada\n")
    except ValueError:
        print("por favor introduza valores enteros\n")
    #except TypeError:
        #print("por favor, introduzca los valores que se le presentan en la pantalla\n")
    #except IndexError:
        #print("por favor, seleccione las filas y columnas presentadas en pantlla\n")
    #except Exception as e:
        #print(f"Se produjo un error desconocido: {e}")

def showRoom(roomConfigId, tempReservations=None):
    #Muestra el estado de la sala seleccionada, incluyendo reservas temporales si las hay.

    try:
        roomConfig = getEntityByProperties(EntitiesFields.ROOM_CONFIGURATION, [EntitiesFields.ID], roomConfigId)
        room = getEntityByProperties(EntitiesFields.ROOM, [EntitiesFields.ID], roomConfig[EntitiesFields.CONFIG_ROOM_ID])
        values = listByProperties(EntitiesFields.RESERVATION, [EntitiesFields.RESERVATION_ROOM_ID, EntitiesFields.DELETED], roomConfigId, False)

        arr = [[0 for _ in range(room[EntitiesFields.ROOM_COLUMNS])] for _ in range(room[EntitiesFields.ROOM_ROWS])]

        for value in values:
            arr[value[EntitiesFields.RESERVATION_ROW] - 1][value[EntitiesFields.RESERVATION_COLUMN] - 1] = 1

        if tempReservations:
            for temp in tempReservations:
                arr[temp[EntitiesFields.RESERVATION_FIELDS[5]] - 1][temp[EntitiesFields.RESERVATION_FIELDS[6]] - 1] = 2

        for column in arr:
            row = ''
            for i in column:
                if i == 0:
                    row += '⬛'  # Disponible
                elif i == 1:
                    row += '🟥'  # Reservado permanentemente
                elif i == 2:
                    row += '🟩'  # Reservado temporalmente
            print("--------------------------------")
            print(row)

    except ValueError:
        print("Por favor introduzca valores enteros\n")
    #except TypeError:
        #print("Por favor, introduzca los valores que se le presentan en la pantalla\n")
   # except Exception as e:
       # print(f"Se produjo un error desconocido: {e}")


def checkAvailable(roomId, row, column, tempReservations=None):
    # Verificar en reservas guardadas
    found = getEntityByProperties(
        EntitiesFields.RESERVATION,
        [EntitiesFields.RESERVATION_ROOM_ID, EntitiesFields.RESERVATION_ROW, EntitiesFields.RESERVATION_COLUMN, EntitiesFields.DELETED],
        roomId, row, column, False
    )
    if found is not None:
        return False

    # Verificar en reservas temporales
    if tempReservations:
        for temp in tempReservations:
            if temp[EntitiesFields.RESERVATION_FIELDS[5]] == row and temp[EntitiesFields.RESERVATION_FIELDS[6]] == column:
                return False

    return True

def checkRoom():
    #función para consultar el estado de la sala seleccionada
    printEntities(EntitiesFields.ROOM_CONFIGURATION)
    try:
        roomConfigId = int(input("\nintroduzca el id de la sala: "))
        clear()
        showRoom(roomConfigId)
    except ValueError:
        print("por favor, introduzca el id como entero\n")
    #TODO modificar para que el día este en may{usculas o minúsculas, y verificar el ingreso del horario

def checkReservations(userId):
    #función para consultar las reservas realizadas por el usuario actual
    reservas = listByProperties(EntitiesFields.RESERVATION,[EntitiesFields.RESERVATION_USER_ID,EntitiesFields.DELETED],userId,False)
    printCustomEntities(reservas,"RESERVATION")

def checkBounds(roomConfigId,row,column):
    roomConfig = getEntityByProperties(EntitiesFields.ROOM_CONFIGURATION, [EntitiesFields.ID], roomConfigId)
    room = getEntityByProperties(EntitiesFields.ROOM, [EntitiesFields.ID], roomConfig[EntitiesFields.CONFIG_ROOM_ID])
    roomRow = room[EntitiesFields.ROOM_COLUMNS]
    roomColumn= room[EntitiesFields.ROOM_ROWS]

    if row > roomRow or column > roomColumn:
        return False
    else:
        return True