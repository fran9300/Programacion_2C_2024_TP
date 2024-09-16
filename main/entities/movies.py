from numeration import getNumberFromSecuence
from entities.utils import getById


# [id,nombre,duracion,descripcion,genero,edad,fechaDeEstreno]
movies = [
    [1,"DeadPool",127,"Superheroes","Accion","18","20/07/2024"],
    [2,"Alien",112,"Pelicula de alien","Suspenso","16","20/09/2024"],
    [3,"Longlegs",100,"pelicula de terror","Terror","13","20/08/2024"]
]


def getMovies():
    return movies


#Función para agregar películas al sistema
def addMovie():
    global movies
    newMovie = []
    newMovie.append(getNumberFromSecuence("movieNumeration"))
    newMovie.append(input("Ingrese nombre de pelicula: "))
    newMovie.append(int(input("Ingrese duracion: ")))
    newMovie.append(input("Ingrese descripcion: "))    
    newMovie.append(input("Ingrese género: "))
    newMovie.append(input("Ingrese edad: "))
    newMovie.append(input("Ingrese fecha de estreno (formato DD/MM/YYYY): "))
    print(newMovie)
    movies.append(newMovie)
    print("Nueva pelicula agregada\t")


#Función para editar películas. Como parametro el pasamos el id de la película Puede editar mas de un campo a la vez y
#finalizar la edicion cuando el usuario lo desee
def editMovie(movieId):
    global movies
    movieToEdit = None
    for movie in movies:
        if movie[0] == movieId:
            movieToEdit = movie

    if not movieToEdit:
        print("No se encontró ninguna película con ID:", movieId)
    else:
        bandera = True
        while bandera:
            print("Editando la película:", movieToEdit)
            print("Seleccione el campo que desea editar:")
            print("1. Nombre de la película")
            print("2. Duración")
            print("3. Descripción")
            print("4. Género")
            print("5. Edad recomendada")
            print("6. Fecha de estreno")
            print("7. Terminar de editar")

            choice = int(input())  # Esta línea debe estar dentro del bucle

            if choice == 1:
                print("Ingrese el nuevo nombre de la película:")
                movieToEdit[1] = input()
            elif choice == 2:
                print("Ingrese la nueva duración:")
                movieToEdit[2] = int(input())
            elif choice == 3:
                print("Ingrese la nueva descripción:")
                movieToEdit[3] = input()
            elif choice == 4:
                print("Ingrese el nuevo género:")
                movieToEdit[4] = input()
            elif choice == 5:
                print("Ingrese la nueva edad recomendada:")
                movieToEdit[5] = input()
            elif choice == 6:
                print("Ingrese la nueva fecha de estreno (formato YYYYMMDD):")
                movieToEdit[6] = input()
            elif choice == 7:
                bandera = False
                print("Edición finalizada")
            else:
                print("Opción no válida.")

            print("Película con ID", movieId, "ha sido actualizada.")
            print("Resultado:", movieToEdit)

    return movies


def deleteMovie(peliculaId, peliculas):
    #Función para eliminar película. Reutilizamos la función getById

    movieToDelete = getById(peliculaId, peliculas)
    
    if movieToDelete == -1:
        print("No se encontró ninguna película con ID: ", peliculaId)
    else:
        peliculas.remove(movieToDelete)
        print("\nPelícula con ID ",peliculaId, " ha sido eliminada.\n")

    return peliculas


def imprimirPeliculas(peliculas):
    #Función que muestra la cartelera
    print("ID | Nombre | Duración | Género | Clasificación")
    for pelicula in peliculas:
        print(f"{pelicula[0]} | {pelicula[1]} | {pelicula[2]} minutos | {pelicula[4]} | +{pelicula[5]}")
    print()
    return None

