
secuences = {
    "userNumeration" : 0,
    "movieNumeration" : 0
}


def getFromDb():
    #Esto devuelve los datos de la secuencia en un diccionario. Key : nombre de secuencia, value: valor de la secuencia
    return None

#Llamar esta funcion cadda vez que se inicia el programa para cargar las secuencias desde la "BD"
def loadSecuences():
    global secuences
    secuences = getFromDb()


def getSecuences():
    return secuences

def getNumberFromSecuence(key):
    global secuences
    number = secuences[key]
    secuences[key] += 1
    return number 