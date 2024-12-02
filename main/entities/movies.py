

from repositories.repository import addEntity, updateEntity, getEntityById, loadData, deleteById, printEntities
from entities.EntitiesFields import MOVIES_FIELDS
from entities import EntitiesFields
from utils.translator import getTranslation


#Abm reservas

def addMovie():
    #funcion para agregar nuevas películas
    try:
        newMovie = {
            "type": "MOVIES",
            #TODO:CAMBIAR A LOS FIELDS, no con los numeros
            EntitiesFields.MOVIES_FIELDS[1]: input("Ingrese nombre de la película: "),
            EntitiesFields.MOVIES_FIELDS[2]: input("Ingrese duración en minutos: "),
            EntitiesFields.MOVIES_FIELDS[3]: input("Ingrese género de la película: "),
            EntitiesFields.MOVIES_FIELDS[4]: input("Ingrese categoría de la película: "),
            EntitiesFields.MOVIES_FIELDS[5]: input("Ingrese edad recomendada: "),
            EntitiesFields.MOVIES_FIELDS[6]: input("Ingrese fecha de estreno (formato DD/MM/YYYY): "),
            EntitiesFields.DELETED : False
        }
        confirmacion = int(input("\npresione 1 para confirmar, 0 para cancelar: "))
    except ValueError:
        print("\ningrese solo valores numéricos para la duración de la película\n")
    else:
        if confirmacion == 1:
            addEntity(newMovie)
            print("\nNueva película agregada al sistema.\n")
        else:
            print("\noperacion cancelada\n")


def editMovie():
    #funcion para editar películas existentes
    try:
        movieId = int(input("Ingrese el ID de la película a editar: "))
        movieToEdit = getEntityById(EntitiesFields.MOVIES, movieId)

        if not movieToEdit:
            print("No se encontró ninguna película con ID:", movieId)
        else:
            movieToEdit[EntitiesFields.TYPE] = EntitiesFields.MOVIES
            editing = True
            while editing:
                print("\nEditando la película:", movieToEdit)
                print("Seleccione el campo que desea editar:")
                for index in range(1, len(MOVIES_FIELDS)):
                    field = MOVIES_FIELDS[index]
                    field = getTranslation(field)
                    print(f"{index}. {field}")
                print(f"{len(MOVIES_FIELDS)}. Terminar de editar\n")

                choice = int(input("Elige una opción: "))
                if choice == len(MOVIES_FIELDS):
                    editing = False
                    print("\nEdición finalizada.")
                elif 1 <= choice < len(MOVIES_FIELDS):
                    field = MOVIES_FIELDS[choice]
                    fieldTrans = getTranslation(field)
                    newValue = input(f"Ingrese el nuevo valor para {fieldTrans}: ")
                    movieToEdit[field] = newValue
                else:
                    print("Opción no válida.")

            # Actualizar la entidad en la base de datos
            updateEntity(movieToEdit)
    except ValueError:
        print("valor mal introducido, por favor ingrese los mismos segun lo indicado en pantalla\n")


def deleteMovie():
    #funcion para borrar peliculas existentes utilizando la funcion generica printEntities
    deleteById(EntitiesFields.MOVIES)


def printMovies():
    #funcion para imprimir películas utilizando la funcion generica printEntities
    printEntities(EntitiesFields.MOVIES)







