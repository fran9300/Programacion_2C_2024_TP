from entities import entitiesEnum
#A la hora de usar archivos se debe usar esto para que los paths esten encapsulados. En caso de mover los archivos solo habra que modificar el path aca.

paths = {
    entitiesEnum.USER:"main/repositories/user.json",
    entitiesEnum.MOVIE: "main/repositories/movie.json",
    "ROOM":"main/repositories/nombre a remplazar",
    "PAYMENT_METHODS":"main/repositories/nombre a remplazar",
    "SECUENCE":"main/repositories/secuences.json"
}


def getPath(key):
    #agregar try catch
    key = key.upper()
    response = paths[key]
    return response