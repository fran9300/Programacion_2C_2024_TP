from entities import EntitiesFields
#A la hora de usar archivos se debe usar esto para que los paths esten encapsulados. En caso de mover los archivos solo habra que modificar el path aca.

paths = {
    EntitiesFields.USER:"repositories/files/user.json",
    EntitiesFields.MOVIES: "repositories/files/movies.json",
    "SECUENCE":"repositories/files/secuences.json",
    EntitiesFields.RESERVATION:"repositories/files/reservation.json",
    EntitiesFields.ROOM : "repositories/files/room.json",
    EntitiesFields.ROOM_CONFIGURATION :"repositories/files/room_configuration.json",
    EntitiesFields.INVOICE: "repositories/files/invoice.json",
    EntitiesFields.INVOICE_RESERVATION: "repositories/files/invoice_reservation.json",
    EntitiesFields.USER_PAYMENT: "repositories/files/user_payment.json",
    EntitiesFields.TICKET_VALUE: "repositories/files/ticket_value.json",
    EntitiesFields.PAYMENT_METHODS:"repositories/files/descuentos.json"
}


def getPath(key):
    #agregar try catch
    key = key.upper()
    response = paths[key]
    return response