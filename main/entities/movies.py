from numeration import getNumberFromSecuence
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
