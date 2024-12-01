from entities.EntitiesFields import *
#Se agrega el campo y su traduccion
translations = {
    USER:"Usuario",
    USER_NAME:"Nombre",
    USER_USERNAME:"Nombre de usuario",
    MOVIE_TITLE:"Titulo",
    MOVIE_DURATION:"Duracion",
    MOVIE_GENRE:"Genero",
    MOVIE_CATEGORY:"Categoria",
    MOVIE_RATING:"Edad recomendada",
    MOVIE_RELEASEDATE:"Fecha de lanzamiento",
    "GestionPeliculas":"Gestion de peliculas",
    "GestionSalas":"Gestion de salas",
    "GestionUsuarios":"Gestion de usuarios",
    "configDescuentoPorTipoDePago":"Configuracion de descuentos",
    "imprimirDescuentos":"Imprimir descuentos",
    "CheckUsuarioActual":"Chequear usuario actual(BORRAR?)",
    "LoginMenu":"Volver al menu",
    "viewMovies":"Ver peliculas",
    "loadMovie":"Cargar pelicula",
    "removeMovie":"Remover pelicula",
    "editMovieInfo":"Editar pelicula",
    "volverMenuPrincipal":"Volver al menu principal",
    "Registro":"Registro",
    "IniciarSesion":"Iniciar Sesion",
}


def getTranslation(value):
    try:        
        response = translations[value]
        return response
    except KeyError:
        return value
