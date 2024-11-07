from numeration import getNumberFromSecuence
from entities.utils import getById, clear
from repositories import addEntity, updateEntity, getEntityById, loadData


# [id,nombre,duracion,descripcion,genero,edad,fechaDeEstreno]
movies = [
    [1,"DeadPool",127,"Superheroes","Accion","18","20/07/2024"],
    [2,"Alien",112,"Pelicula de alien","Suspenso","16","20/09/2024"],
    [3,"Longlegs",100,"pelicula de terror","Terror","13","20/08/2024"]
]


def getMovies():
    return movies

def addMovie():
    
    newMovie = {
        "type": "MOVIES",  
        "title": input("Ingrese nombre de la película: "),
        "duration": int(input("Ingrese duración en minutos: ")),
        "description": input("Ingrese descripción de la película: "),
        "genre": input("Ingrese género de la película: "),
        "rating": input("Ingrese edad recomendada: "),
        "release_date": input("Ingrese fecha de estreno (formato DD/MM/YYYY): ")
    }
    
    addEntity(newMovie)
    print("\nNueva película agregada al sistema.\n")



def editMovie():
    movieId = int(input("Ingrese el ID de la película a editar: "))
    movieToEdit = getEntityById("MOVIES", movieId)

    if not movieToEdit:
        print("No se encontró ninguna película con ID:", movieId)
    else:
        bandera = True
        while bandera:
            print("\nEditando la película:", movieToEdit)
            print("Seleccione el campo que desea editar:")
            print("1. Nombre de la película")
            print("2. Duración")
            print("3. Descripción")
            print("4. Género")
            print("5. Edad recomendada")
            print("6. Fecha de estreno")
            print("7. Terminar de editar\n")

            choice = int(input())
            if choice == 1:
                movieToEdit["title"] = input("Ingrese el nuevo nombre de la película: ")
            elif choice == 2:
                movieToEdit["duration"] = int(input("Ingrese la nueva duración: "))
            elif choice == 3:
                movieToEdit["description"] = input("Ingrese la nueva descripción: ")
            elif choice == 4:
                movieToEdit["genre"] = input("Ingrese el nuevo género: ")
            elif choice == 5:
                movieToEdit["rating"] = input("Ingrese la nueva edad recomendada: ")
            elif choice == 6:
                movieToEdit["release_date"] = input("Ingrese la nueva fecha de estreno (formato DD/MM/YYYY): ")
            elif choice == 7:
                bandera = False
                print("\nEdición finalizada.")
            else:
                print("Opción no válida.")

        # Guardar los cambios en el archivo
        updateEntity(movieToEdit)
        print("\nPelícula con ID", movieId, "ha sido actualizada en el sistema.\n")


def deleteMovie():
    movieId = int(input("Ingrese el ID de la película a eliminar: "))
    movieToDelete = getEntityById("MOVIES", movieId)

    if not movieToDelete:
        print("No se encontró ninguna película con ID:", movieId)
    else:
        movieToDelete["deleted"] = True
        updateEntity(movieToDelete)
        print("\nPelícula con ID", movieId, "ha sido eliminada lógicamente del sistema.\n")



def printMovies():
    movies = loadData("MOVIES")  
    print("ID | Nombre | Duración | Género | Clasificación")
    for movie in movies:
        if not movie.get("deleted", False): 
            print(f"{movie['id']} | {movie['title']} | {movie['duration']} minutos | {movie['genre']} | +{movie['rating']}")
    print()




