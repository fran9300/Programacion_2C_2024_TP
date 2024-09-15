from numeration import getNumberFromSecuence
from utils import getById
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
    movieToDelete = getById(peliculaId, peliculas)
    
    if movieToDelete == -1:
        print("No se encontró ninguna película con ID: ", peliculaId)
    else:
        peliculas.remove(movieToDelete)
        print("Película con ID ",peliculaId, " ha sido eliminada.")

    return peliculas

def imprimirPeliculas(peliculas):
    print("ID | Nombre | Duración | Género | Clasificación")
    for pelicula in peliculas:
        print(f"{pelicula[0]} | {pelicula[1]} | {pelicula[2]} minutos | {pelicula[4]} | +{pelicula[5]}")
    return ""


print (editMovie(1))

movieId= print ("Ingrese el numero de la pelicula que quiere eliminar: ")
print (deleteMovie(movieId,movies))