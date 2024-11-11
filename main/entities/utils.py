import os
from entities import EntitiesFields

def getById(id,arr):

    filtered = list(filter(lambda value : value[EntitiesFields.ID]==id,arr))
    return filtered[0] if (filtered != None and len(filtered)>0 )else -1

clear = lambda: os.system('cls')

