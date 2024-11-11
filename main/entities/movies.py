

from repositories.repository import addEntity, updateEntity, getEntityById, loadData, deleteById, printEntities
from entities.EntitiesFields import MOVIES_FIELDS
from entities import EntitiesFields


#Abm reservas

def getMovies():
    #Borrar esto dsp 
    return None



def addMovie():
    try:
        newMovie = {
            "type": "MOVIES",
            EntitiesFields.MOVIES_FIELDS[1]: input("Ingrese nombre de la película: "),
            EntitiesFields.MOVIES_FIELDS[2]: int(input("Ingrese duración en minutos: ")),
            EntitiesFields.MOVIES_FIELDS[3]: input("Ingrese género de la película: "),
            EntitiesFields.MOVIES_FIELDS[4]: input("Ingrese categoría de la película: "),
            EntitiesFields.MOVIES_FIELDS[5]: input("Ingrese edad recomendada: "),
            EntitiesFields.MOVIES_FIELDS[6]: input("Ingrese fecha de estreno (formato DD/MM/YYYY): "),
            EntitiesFields.DELETED : False
        }
        confirmacion = int(input("\npresione 1 para confirmar, 0 para cancelar: "))
    except ValueError:
        print("\ningrese solo valores numéricos para la duración de la película\n")
    else:
        if confirmacion == 1:
            addEntity(newMovie)
            print("\nNueva película agregada al sistema.\n")
        else:
            print("\noperacion cancelada\n")


def editMovie():
    movieId = int(input("Ingrese el ID de la película a editar: "))
    movieToEdit = getEntityById("MOVIE", movieId)

    if not movieToEdit:
        print("No se encontró ninguna película con ID:", movieId)
    else:
        editing = True
        while editing:
            print("\nEditando la película:", movieToEdit)
            print("Seleccione el campo que desea editar:")
            for index in range(1, len(MOVIES_FIELDS)):
                field = MOVIES_FIELDS[index]
                print(f"{index}. {field.capitalize()}")
            print(f"{len(MOVIES_FIELDS)}. Terminar de editar\n")

            choice = int(input("Elige una opción: "))
            if choice == len(MOVIES_FIELDS):
                editing = False
                print("\nEdición finalizada.")
            elif 1 <= choice < len(MOVIES_FIELDS):
                field = MOVIES_FIELDS[choice]
                newValue = input(f"Ingrese el nuevo valor para {field}: ")

                
                if field == "year":
                    newValue = int(newValue)
                elif field == "rating":
                    newValue = float(newValue)

                movieToEdit[field] = newValue
            else:
                print("Opción no válida.")

        # Actualizar la entidad en la base de datos
        updateEntity(movieToEdit)



def deleteMovie():
    deleteById(EntitiesFields.MOVIES)



def printMovies():
    printEntities(EntitiesFields.MOVIES)







