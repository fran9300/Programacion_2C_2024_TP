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

def addMovie():
    global movies
    newMovie = []
    newMovie.append(getNumberFromSecuence("movieNumeration"))
    print("Ingrese nombre de pelicula")
    newMovie.append(input())
    print("Ingrese duracion")
    newMovie.append(int(input)())
    print("Ingrese descripcion")
    newMovie.append(input())    
    print("Ingrese género")
    newMovie.append(input())
    print("Ingrese edad")
    newMovie.append(input())
    print("Ingrese fecha de estreno (formato DD/MM/YYYY)")
    newMovie.append(input())
    print(newMovie)
    movies.append(newMovie)
    print("Nueva pelicula agregada")
    print(movies)



def editMovie(movieId):
    global movies
    movieToEdit = None
    for movie in movies:
        if movie[0] == movieId:
            movieToEdit = movie

    if not movieToEdit:
        print ("No se encontró ninguna pelicula con ID: ", movieId)
    else:
        #TODO: meter dentro d un while
        print("Editando la película: ", movieToEdit)

        print("Seleccione el campo que desea editar:")
        print("1. Nombre de la película")
        print("2. Duración")
        print("3. Descripción")
        print("4. Género")
        print("5. Edad recomendada")
        print("6. Fecha de estreno")

        choice = int(input())

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
        else:
            print("Opción no válida.")
            return movies

        print("Película con ID", movieId, " ha sido actualizada.")
        print("Resultado: ", movieToEdit)



def removeMovie(movies, movieId):
    movieToRemove = [movie for movie in movies if movie[0] == movieId] #Uso listas por comprension 
    if movieToRemove:
        movies = [movie for movie in movies if movie[0] != movieId]
        print ("Pelicula con ID ", movieId, "eliminada")
    else:
        print("No se encontró ninguna película con ID ", movieId)
    
    return movies


def imprimirPeliculas():
    # TODO: imprime los datos de archivo de peliculas
    # @AgustinaMieres
    # sale por pantalla:
    # id | nombre | duracion | edad | ..
    # 1| deadpool | 120 | +18
    # 2 | alien | 130 | +16
    return None