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
    TICKET_VALUE_VALUE:"Valor de la entrada",
    
    "GestionPeliculas":"Gestion de peliculas",
    "viewMovies":"Ver peliculas",
    "loadMovie":"Cargar pelicula",
    "removeMovie":"Remover pelicula",
    "editMovieInfo":"Editar pelicula",

    "GestionSalas":"Gestion de salas",
    "consultarSalas": "Consultar salas",
    "crearSala":"Crear sala",
    "eliminarSala":"Eliminar sala",
    "CrearFuncionDePelicula":"crear funcion de pelicula",
    "MostrarFuncionesProgramadas":"Mostrar funciones programadas",
    "EliminarFuncionProgramada":"Eliminar funcion programada",
    "liberarSala":"liberar sala",
    "VerificarPrecioEntrada":"Verificar el precio de la entrada",
    "ModificarValorEntrada":"Modificar el valor de la entrada",
    
    
    "GestionUsuarios":"Gestion de usuarios",
    "configDescuentoPorTipoDePago":"Configuracion de descuentos",
    "imprimirDescuentos":"Imprimir descuentos",
    "CheckUsuarioActual":"Chequear usuario actual",
    "LoginMenu":"Volver al menu de login",
    
    "viewUsers":"Ver usuarios",
    "AgregarNuevoUsuario":"Agregar nuevo usuario",
    "editUSerInfo":"Editar informacion de usuarios",
    "eliminarUsuario":"Eliminar usuarios",

    "configurarDescuentos":"Configurar descuentos",
    "cargarSaldoUsuario":"Cargar saldo",
    "listarSaldosUsuario":"Ver mis saldos",

    "CheckearReservasSalas":"Ver estado de las salas",
    "ReservarEntradas":"Reservar entradas",
    "VerMisReservas":"Ver mis reservas",
    "ConfigurarUsuario": "Configuración",
    "volverMenuPrincipal":"Volver al menu principal",
    "Registro":"Registro",
    "IniciarSesion":"Iniciar Sesion",
    "checkTicketValue":"Chequear precio de entrada",
    "updateTicketValue":"Actualizar precio de entrada",
}


def getTranslation(value):
    try:        
        response = translations[value]
        return response
    except KeyError:
        return value


def getOriginal(valueT):
    try:        
        for key,value in translations.items():
            if(value == valueT):
                return key        
        return valueT
    except:
        return value
    