

from repositories.repository import addEntity, updateEntity, getEntityById, loadData, deleteById, printEntities
from entities import EntitiesFields


#Abm reservas

def getMovies():
    #Borrar esto dsp 
    return None



def addMovie():
    newMovie = {
        "type": "MOVIES",
        EntitiesFields.MOVIES_FIELDS[0]: input("Ingrese nombre de la película: "),
        EntitiesFields.MOVIES_FIELDS[1]: int(input("Ingrese duración en minutos: ")),
        EntitiesFields.MOVIES_FIELDS[2]: input("Ingrese descripción de la película: "),
        EntitiesFields.MOVIES_FIELDS[3]: input("Ingrese género de la película: "),
        EntitiesFields.MOVIES_FIELDS[4]: input("Ingrese edad recomendada: "),
        EntitiesFields.MOVIES_FIELDS[5]: input("Ingrese fecha de estreno (formato DD/MM/YYYY): ")
    }
    
    addEntity(newMovie)
    print("\nNueva película agregada al sistema.\n")



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
    printEntities("USER")







