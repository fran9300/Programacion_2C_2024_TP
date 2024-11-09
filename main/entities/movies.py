from numeration import getNumberFromSecuence
from entities.utils import getById, clear
from repositories.repository import addEntity, updateEntity, getEntityById, loadData, deleteById
from main.entities import EntitiesFields
from main.entities.EntitiesFields import MOVIES_FIELDS







def addMovie():
    newMovie = {
        "type": "MOVIES",
        MOVIES_FIELDS[1]: input("Ingrese nombre de la película: "),
        MOVIES_FIELDS[2]: int(input("Ingrese duración en minutos: ")),
        MOVIES_FIELDS[3]: input("Ingrese descripción de la película: "),
        MOVIES_FIELDS[4]: input("Ingrese género de la película: "),
        MOVIES_FIELDS[5]: input("Ingrese edad recomendada: "),
        MOVIES_FIELDS[6]: input("Ingrese fecha de estreno (formato DD/MM/YYYY): ")
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
            for key, value in MOVIES_FIELDS.items():
                print(f"{key}. {value.capitalize()}")
            print("7. Terminar de editar\n")

            choice = int(input("Elige una opción: "))
            if choice == 7:
                editing = False
                print("\nEdición finalizada.")
            elif choice in MOVIES_FIELDS:
                field = MOVIES_FIELDS[choice]
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
    movies = loadData("MOVIES")  
    print("ID | Nombre | Duración | Género | Clasificación")
    for movie in movies:
     if not movie.get("deleted", False): 
        print(f"{movie['id']} | {movie[MOVIES_FIELDS[1]]} | {movie[MOVIES_FIELDS[2]]} minutos | {movie[MOVIES_FIELDS[4]]} | +{movie[MOVIES_FIELDS[5]]}")
print()





