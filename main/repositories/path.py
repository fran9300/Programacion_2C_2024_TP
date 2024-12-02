from entities import EntitiesFields
#A la hora de usar archivos se debe usar esto para que los paths esten encapsulados. En caso de mover los archivos solo habra que modificar el path aca.

paths = {
    EntitiesFields.USER:"main/repositories/user.json",
    EntitiesFields.MOVIES: "main/repositories/movies.json",
    "PAYMENT_METHODS":"main/repositories/nombre a remplazar",
    "SECUENCE":"main/repositories/secuences.json",
    EntitiesFields.RESERVATION:"main/repositories/reservation.json",
    EntitiesFields.ROOM : "main/repositories/room.json",
    EntitiesFields.ROOM_CONFIGURATION :"main/repositories/room_configuration.json",
    EntitiesFields.INVOICE: "main/repositories/invoice.json",
    EntitiesFields.INVOICE_RESERVATION: "main/repositories/invoice_reservation.json",
    EntitiesFields.USER_PAYMENT: "main/repositories/user_payment.json",
    EntitiesFields.TICKET_VALUE: "main/repositories/ticket_value.json"
}


def getPath(key):
    #agregar try catch
    key = key.upper()
    response = paths[key]
    return response