def loadUsers():
    return None

def loadMovies():
    return None

def loadRooms():
    return None

def loadPaymentMethods():
    return None


def logicDelete():
    #Se debe permitir eliminar una entidad de manera logica. Evitar borrado fisco.
    return None

def createTransaction():
    #@fpelli: se debe crear concepto de transaccionalidad.
    return None

def autoInsertId(entidad):
    #@aMieres: se debe crear una funcion que cuando le llegue una entidad, busque la secuencia y obtenga su valor, se lo asigne a la entidad y devuelva la entidad
    
    return entidad


def updateEntity():
    #debe permitir modificar una entidad y savear el archivo. Tiene que remplazar la entidad. por ejemplo si se cambia el campo duracion de 90 -> 120. 
    # Tiene que aparecer 120 en el archivo. pero no crear un nuevo movie sino que remplazar el existente
    return None

# agrgar a todas las entidades un campo deleted para hacer borrado logico.
# EN las entidades agregar un campo que discrimine que tipo es. Luego se busca el path del archivo correspondiente por el tipo de entidad y se guarda ahi.
#  Esto lo vamos a usar para hcer un metodo generico de creacion de entidad