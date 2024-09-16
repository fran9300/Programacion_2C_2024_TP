
secuences = {
    "userNumeration" : 4,
    "movieNumeration" : 4,
    "salaNumeration" : 4
}


def getFromDb():
    #Esto devuelve los datos de la secuencia en un diccionario. Key : nombre de secuencia, value: valor de la secuencia
    return None

def loadSecuences():
    #Llamar esta funcion cada vez que se inicia el programa para cargar las secuencias desde la "BD"
    global secuences
    secuences = getFromDb()


def getSecuences():
    return secuences

def getNumberFromSecuence(key):
    global secuences
    number = secuences[key]
    secuences[key] += 1
    return number 