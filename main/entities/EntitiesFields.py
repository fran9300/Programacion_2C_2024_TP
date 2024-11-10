# entities_enum.py

USER = "USER"
MOVIES = "MOVIES"
SECUENCE = "SECUENCE"
RESERVATION = "RESERVATION"
ROOM = "ROOM"
ROOM_CONFIGURATION = "ROOM_CONFIGURATION"
#general properties
ID = "id"
DELETED = "deleted"
TYPE = "type"


#Room properties

ROOM_NAME = "name"
ROOM_ROWS = "rows"
ROOM_COLUMNS = "columns"
ROOM_FIELDS = [ID,ROOM_NAME,ROOM_ROWS,ROOM_COLUMNS]
#Room configuration proeprties

CONFIG_ROOM_ID = "roomId"
CONFIG_TIME = "time"
CONFIG_MOVIE_ID = "movieId"
CONFIG_DAY = "day"

# reservation properties

RESERVATION_ROOM_ID = "roomId"
RESERVATION_USER_ID = "userId"
RESERVATION_ROW = "row"
RESERVATION_COLUMN = "column"



# Diccionario para los campos de la entidad MOVIES
MOVIES_FIELDS = {
    1: "title",
    2: "duration",
    3: "description",
    4: "genre",
    5: "rating",
    6: "release_date"
}
#TODO: que qude como el resto de properties


# entitiesEnum.py

USERS_FIELDS = {
    1: "username",
    2: "first_name",
    3: "last_name",
    4: "password",
    5: "access_level",
    6: "birthdate",
    7: "email",
    8: "balance"
}
#TODO: que qude como el resto de properties, obviamente arreglar donde se llamaban a estos campos

FIELDS = {
    USER: "USER",#agregar los fields de cada entidad
    MOVIES: "MOVIES",
    SECUENCE: "SECUENCE",
    RESERVATION: "RESERVATION",
    ROOM: ROOM_FIELDS,
    ROOM_CONFIGURATION: "ROOM_CONFIGURATION",
}
