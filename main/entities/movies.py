

from repositories.repository import addEntity, updateEntity, getEntityById, loadData, deleteById, printEntities
from entities import EntitiesFields




def getMovies():
    #Borrar esto dsp 
    return None



def addMovie():
    # Crea una nueva película usando las constantes de EntitiesFields para cada campo
    newMovie = {
        EntitiesFields.TYPE: EntitiesFields.MOVIES,
        EntitiesFields.MOVIE_TITLE: input("Ingrese nombre de la película: "),
        EntitiesFields.MOVIE_DURATION: int(input("Ingrese duración en minutos: ")),
        EntitiesFields.MOVIE_DESCRIPTION: input("Ingrese descripción de la película: "),
        EntitiesFields.MOVIE_GENRE: input("Ingrese género de la película: "),
        EntitiesFields.MOVIE_RATING: input("Ingrese edad recomendada: "),
        EntitiesFields.MOVIE_RELEASE_DATE: input("Ingrese fecha de estreno (formato DD/MM/YYYY): ")
    }
    
    addEntity(newMovie)
    print("\nNueva película agregada al sistema.\n")

from entities import EntitiesFields
from repositories.repository import getEntityById, updateEntity

def editMovie():
    movieId = int(input("Ingrese el ID de la película a editar: "))
    movieToEdit = getEntityById(EntitiesFields.MOVIES, movieId)

    if not movieToEdit:
        print("No se encontró ninguna película con ID:", movieId)
    else:
        editing = True
        while editing:
            print("\nEditando la película:", movieToEdit)
            print("Seleccione el campo que desea editar:")
            print("1. Título")
            print("2. Duración")
            print("3. Descripción")
            print("4. Género")
            print("5. Clasificación")
            print("6. Fecha de estreno")
            print("7. Terminar de editar\n")

            choice = int(input("Elige una opción: "))
            if choice == 7:
                editing = False
                print("\nEdición finalizada.")
            else:
                # Mapa de opciones a los campos correspondientes en EntitiesFields
                field_map = {
                    1: EntitiesFields.MOVIE_TITLE,
                    2: EntitiesFields.MOVIE_DURATION,
                    3: EntitiesFields.MOVIE_DESCRIPTION,
                    4: EntitiesFields.MOVIE_GENRE,
                    5: EntitiesFields.MOVIE_RATING,
                    6: EntitiesFields.MOVIE_RELEASE_DATE
                }

                if choice in field_map:
                    field = field_map[choice]
                    newValue = input(f"Ingrese el nuevo valor para {field}: ")
                    
                    if field == EntitiesFields.MOVIE_DURATION:
                        try:
                            newValue = int(newValue)
                        except ValueError:
                            print("Duración inválida. Debe ser un número entero.")
                            continue
                    
                    movieToEdit[field] = newValue
                else:
                    print("Opción no válida.")

        
        updateEntity(movieToEdit)
        print("\nPelícula con ID", movieId, "ha sido actualizada en el sistema.\n")



def deleteMovie():
    deleteById(EntitiesFields.MOVIES) #Aca no deberia pasarle algun id?



def printMovies():
    printEntities(EntitiesFields.MOVIES)





