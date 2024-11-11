

from repositories.repository import addEntity, updateEntity, getEntityById, loadData, deleteById, printEntities
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
    movieToEdit = getEntityById("MOVIES", movieId)

    if not movieToEdit:
        print("No se encontró ninguna película con ID:", movieId)
    else:
        editing = True
        while editing:
            print("\nEditando la película:", movieToEdit)
            print("Seleccione el campo que desea editar:")
            for key, value in EntitiesFields.MOVIES_FIELDS.items():
                print(f"{key}. {value.capitalize()}")
            print("7. Terminar de editar\n")

            choice = int(input("Elige una opción: "))
            if choice == 7:
                editing = False
                print("\nEdición finalizada.")
            elif choice in EntitiesFields.MOVIES_FIELDS:
                field = EntitiesFields.MOVIES_FIELDS[choice]
                newValue = input(f"Ingrese el nuevo valor para {field}: ")
                movieToEdit[field] = newValue
            else:
                print("Opción no válida.")

        # Guardar los cambios en el archivo
        updateEntity(movieToEdit)
        print("\nPelícula con ID", movieId, "ha sido actualizada en el sistema.\n")

def deleteMovie():
    deleteById(EntitiesFields.MOVIES)



def printMovies():
    printEntities("MOVIES")







