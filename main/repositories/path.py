from entities import EntitiesFields
#A la hora de usar archivos se debe usar esto para que los paths esten encapsulados. En caso de mover los archivos solo habra que modificar el path aca.

paths = {
    EntitiesFields.USER:"main/repositories/files/user.json",
    EntitiesFields.MOVIES: "main/repositories/files/movies.json",
    "SECUENCE":"main/repositories/files/secuences.json",
    EntitiesFields.RESERVATION:"main/repositories/files/reservation.json",
    EntitiesFields.ROOM : "main/repositories/files/room.json",
    EntitiesFields.ROOM_CONFIGURATION :"main/repositories/files/room_configuration.json",
    EntitiesFields.INVOICE: "main/repositories/files/invoice.json",
    EntitiesFields.INVOICE_RESERVATION: "main/repositories/files/invoice_reservation.json",
    EntitiesFields.USER_PAYMENT: "main/repositories/files/user_payment.json",
    EntitiesFields.TICKET_VALUE: "main/repositories/files/ticket_value.json",
}


def getPath(key):
    #agregar try catch
    key = key.upper()
    response = paths[key]
    return response