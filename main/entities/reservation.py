from entities import EntitiesFields
from repositories.repository import getEntityByProperties,addEntity,listByProperties, printCustomEntities,printEntities
from entities.movies import printMovies
from entities.utils import clear

valorEntrada = 5000

def addReservation(userId):
    #permite agregar una nueva reservacion de butacas por parte del usuario. 
    try:
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
            
            if checkAvailable(sala_reserva["id"],fila_aciento_reserva,columna_aciento_reserva):
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
                    addEntity(newReservation)
                    clear()
                    print("\nNueva reserva guardada.\n")
                    showRoom(sala_reserva["id"])
                    i += 1
            else:
                print("\nasiento ya reservado, por favor seleccione otro.\n")

        if cantidad_entradas != 0:
            importe = cantidad_entradas * valorEntrada
            print(f"\nReserva del usuario numero: {userId}")
            print(f"importe total de :{importe} pesos\n")
        else:
            clear()
            print("operación cancelada\n")
    except ValueError:
        print("por favor introduza valores enteros\n")
    except TypeError:
        print("por favor, introduzca los valores que se le presentan en la pantalla\n")
    except IndexError:
        print("por favor, seleccione las filas y columnas presentadas en pantlla\n")
    except Exception as e:
        print(f"Se produjo un error desconocido: {e}")

def showRoom(roomConfigId):
    #función para mostrar el estado de la sala seleccionada
    try:
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
    except ValueError:
        print("por favor introduza valores enteros\n")
    except TypeError:
        print("por favor, introduzca los valores que se le presentan en la pantalla\n")
    except Exception as e:
        print(f"Se produjo un error desconocido: {e}")

def checkAvailable(roomId,row,column):
    #función para chequear si una butaca se encuentra disponible o no, en una sala especifica
    found = getEntityByProperties(EntitiesFields.RESERVATION,[EntitiesFields.RESERVATION_ROOM_ID,EntitiesFields.RESERVATION_ROW,EntitiesFields.RESERVATION_COLUMN,EntitiesFields.DELETED],roomId,row,column,False)
    if found != None:
        return False
    return False if found else True

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
