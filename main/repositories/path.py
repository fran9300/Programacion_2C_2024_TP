
#A la hora de usar archivos se debe usar esto para que los paths esten encapsulados. En caso de mover los archivos solo habra que modificar el path aca.

paths = {
    "USER":"main/repositories/user.json",
    "MOVIE":"main/repositories/nombre a remplazar",
    "ROOM":"main/repositories/nombre a remplazar",
    "PAYMENT_METHODS":"main/repositories/nombre a remplazar",
    "SECUENCE":"main/repositories/secuences.json"
}


def getPath(key):
    #agregar try catch
    key = key.upper()
    response = paths[key]
    return response