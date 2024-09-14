# TODAS LAS "ENTIDADES" EN SU PRIMER CAMPO TIENE EL ID
    # [
    #     [id,nombre,duracion],
    #     [id,nombre,duracion],
    #     [id,nombre,duracion],
    # ]


# [id,nombre,duracion,descripcion,genero,edad,fechaDeEstreno]
peliculas = [
    [1,"DeadPool",127,"Superheroes","Accion","18","20/07/2024"],
    [2,"Alien",112,"Pelicula de alien","Suspenso","16","20/09/2024"],
    [3,"Longlegs",100,"pelicula de terror","Terror","13","20/08/2024"]
]
# [id,nombre,filas,columnas]
salas = [
    [1,"1",25,30],
    [2,"2",20,25],
    [3,"3",30,25]
]
# [id,idSala,horario,fecha]
horarios = [
    [1,1,"1400","0903"],
    [1,2,"1200","0904"],
    [1,2,"1500","0904"],
    [1,3,"1800","0905"]
]

MetodosDePago = [[
    [1,"Cash"],
    [2,"Transfer"],
    [3,"Debt"],
    [4,"Credit"],
    [5,"Points"]
]]
# [id,user,nombre,apellido,password,role,fechaNacimiento,email,saldoTotal]
users= [
    [1,"fpelli","Franco","Pelli","contraseña",2,"20020325","fpelli@uade.edu.ar",100000],
    [2,"ipelli","Ivan","Pelli","contraseña123",2,"20061010","ipelli@uade.edu.ar",50000],
    [3,"admin","","","admin",1,"20000101","admin@uade.edu.ar",100000]
]
roles = [
    [1,"admin"],
    [2,"client"]
]

# [id,userId,metodoDePagoId]
userPayment = [
    [1,1,1],
    [2,1,3],
    [3,2,2]
]

DESCUENTOS = {
    "Cash": 0.30,     # 30% descuento
    "Transfer": 0.20, # 20% descuento
    "Debt": 0.10,     # 10% descuento
    "Credit": 0.02,   # 2% descuento
    # Para "Points" se manejará en una función aparte
}

METODOSDEPAGO = {
    1: "Cash",
    2: "Transfer",
    3: "Debt",
    4: "Credit",
    5: "Points"
}

# TODO: hacer busqueda por id en array (onlyRead)

def getById(id,arr):
    filtered = list(filter(lambda value : value[0]==id,arr))
    return filtered[0] if (filtered != None and len(filtered)>0 )else -1 



def  login():
    # TODO: login
    return None

def imprimirPeliculas():
    # TODO: imprime los datos de archivo de peliculas
    # @AgustinaMieres
    # sale por pantalla:
    # id | nombre | duracion | edad | ..
    # 1| deadpool | 120 | +18
    # 2 | alien | 130 | +16
    return None

def asignarPeliculaASala():
    imprimirPeliculas()
    # TODO: tiene que mostrar los horarios disponibles en una fecha para sala y poder reservarla
    return None

def crearMatrizSala():
    # TODO: pregunta por filas  y columnas y crea la matriz
    # @fran9300
    return None

def cargarPelicula():
    # TODO: cargar pelicula tiene nombre, duración, edad, descripcion, genero, fecha de estreno y se guarda en un array de peliculas(matriz)
    #@fpelliStudent
    return None

def eliminarPelicula():
    imprimirPeliculas()
    #TODO: eliminar pelicula cargada por id. Llega un array y tiene que eliminar por id . mirar inicio del archivo
    #@fran9300


def cargarHorarios():
    # TODO: cargar horarios a una sala
    # @AgustinaMieres
    return None

def liberarSala():
    #TODO: una vez se cargo una pelicula: se requiere restablecer la sala
    #@fran9300
    return None

def cargarSala():
    # TODO: sala: cantidad de filas, cantidad de columnas, horario, pelicula
    crearMatrizSala()
    cargarHorarios()
    return None
def register():
    # TODO:registrar client y guardarlo en la ""BD"": TODO: definir campos de cliente
    #@fpelliStudent
    return None

def configDescuentoPorTipoDePago(metodo):

    if metodo in DESCUENTOS:
        return DESCUENTOS[metodo]
    else:
        return 0.0

def adminManage():
    login()
    consultarPeliculas()
    cargarPelicula()
    eliminarPelicula()
    cargarSala()
    asignarPeliculaASala()
    configDescuentoPorTipoDePago()
    liberarSala()
    return None

def consultarPeliculas():
    imprimirPeliculas()
    # TODO: Lee el archivo de peliculas y muestra la informacion quiza podemos distinguir entre usuario y admin







def chequeoPago(usuario):
    #TODO: recibe el usuario([]) y
    #TODO: chequea que el cliente tenga saldo disponible para pagar la cantidad de entradas que desea comprar(aplica a todos los tipo de pago)
    # @fran9300
    return None

def imprimirSala():
    #TODO: imprime el estado actual de la sala
    #@fpelliStudent
    return None

def elegirButacas():
    #TODO: retorna la posicion de la butaca elegida formato letra-numero(fila-columna)
    #@AgustinaMieres
    return None
def reservarButaca():
    #recibe nro de butaca y la reserva en array de la sala (lo marca o con 1 o con los datos del cliente)
    #@fran9300
    return None


def calcularTotal(cantidadEntradas):
    #TODO: calcula el total de las entradas
    #@fpelliStudent
    return None

#Funcion para eliminar pelis

def removeMovie(movies, movieId):
    movieToRemove = [movie for movie in movies if movie[0] == movieId] #Uso listas por comprension 

    if movieToRemove:
        movies = [movie for movie in movies if movie[0] != movieId]
        print ("Pelicula con ID ", movieId, "eliminada")
    else:
        print("No se encontró ninguna película con ID ", movieId)
    
    return movies

#Funcion para editar las pelis

def editMovie(movies, movieId):
   
    movieToEdit = None
    for movie in movies:
        if movie[0] == movieId:
            movieToEdit = movie

    if not movieToEdit:
        print ("No se encontró ninguna pelicula con ID: ", movieId)
       
        return movies

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
    return movies


def aplicarPuntos(total):
    while True:
        puntos = input("Ingrese la cantidad de puntos a utilizar (1 punto = 1 peso, o ingrese 0 para no utilizar puntos): ")
        if puntos.isdigit():
            puntos = int(puntos)
            if puntos <= total:
                totalPoints=total-puntos
                return totalPoints
            else:
                print(f"No puede utilizar más puntos de los que corresponden al total ({total} puntos). Intente de nuevo.")
        else:
            print("Debe ingresar un número válido de puntos. Por favor, intente de nuevo.")

def aplicarDescuento (total,metodoID):
    if metodoID==5:
        return total
    else:
        descuento=configDescuentoPorTipoDePago(metodoID)
        valorTotal = total * (1-descuento)
        return valorTotal

def ingresarCuponDescuento(total, codigoDescuento):
    # TODO: if si el codigo es igual a 'DESCUENTO' aplica descuento
    #@fran9300
    return None

def imprimirFactura():
     #@fran9300
    # TODO: generacionFactura()
    #TODO: Imprime los detalles de la compra, datos del cliente, y que butacas se reservaron
    return None

def comprarEntrada():
    consultarPeliculas()
    #elegir pelicula
    #elegir horario que tengan butacas disponibles: muestro todos los horarios  o solo los horarios con butacas disponibles
    # Consultar cantida de entradas
    imprimirSala() # para ver estado actual de la sala
    elegirButacas()
    calcularTotal()

    pedirMetodoDePago()
    aplicarDescuento()
    ingresarCuponDescuento()
    #confirmar
    chequeoPago()
    reservarButaca()
    imprimirFactura()
    return None

def pedirMetodoDePago():
    """
    Solicita al usuario que seleccione un método de pago y retorna la opción seleccionada.
    
    Returns:
        int: El número correspondiente al método de pago seleccionado.
    """
    while True:
        print("Opciones de método de pago:")
        
        
        for numero in METODOSDEPAGO:
            metodo = METODOSDEPAGO[numero]
            print(numero, metodo)
        
        opcion = input("Ingrese el número del método de pago: ")
        
        if opcion.isdigit():  
            opcion = int(opcion)  
            
            if opcion in METODOSDEPAGO:  
                return opcion
            else:
                print("El número ingresado no es válido. Ingrese otro número.")
                
        else:
            print("Debe ingresar un número válido. Por favor, intente de nuevo.")

def clientConfig():
    #TODO: permite modificar los datos del cliente, y su metodo de pago
    return None


def adminConfig():
    # TODO: permite configurar al administrador por ejemplo : precio de entrada, descuentos
    # @fpelliStudent
    return None

def configuracionDelUsuario():
    # if (tipoUsuario)
    clientConfig()
    adminConfig()

def editUser(users):
  
    print("Ingrese el ID del usuario que desea editar:")
    user_id = int(input())

    user = None
    for u in users:
        if u[0] == user_id:
            user = u
    
    if not user:
        print("Usuario no encontrado.")
        return

    print("Seleccione el campo que desea editar:")
    print("1. Nombre de usuario")
    print("2. Nombre")
    print("3. Apellido")
    print("4. Contraseña")
    print("5. Fecha de nacimiento")
    print("6. Correo electrónico")
    print("7. Saldo")

    choice = int(input())

    if choice == 1:
        print("Ingrese el nuevo nombre de usuario:")
        user[1] = input()
    elif choice == 2:
        print("Ingrese el nuevo nombre:")
        user[2] = input()
    elif choice == 3:
        print("Ingrese el nuevo apellido:")
        user[3] = input()
    elif choice == 4:
        print("Ingrese la nueva contraseña:")
        user[4] = input()
    elif choice == 5:
        print("Ingrese la nueva fecha de nacimiento (formato YYYYMMDD):")
        user[6] = input()
    elif choice == 6:
        print("Ingrese el nuevo correo electrónico:")
        user[7] = input()
    elif choice == 7:
        print("Ingrese el nuevo saldo:")
        user[8] = int(input())
    else:
        print("Opción no válida.")
        return

    print("Datos del usuario actualizados:", user)



def clientManage():
    consultarPeliculas()
    comprarEntrada()
    configuracionDelUsuario()
    return ''



# register()
# if ():
#     adminManage()
# else:
#     clientManage()

print("ejemplo getById")
print(getById(2,peliculas))


#Programa principal
metodoDePago=pedirMetodoDePago()
print ("Metodo de pago seleccionado:", metodoDePago)

cantEntradas=int(input("Ingrese la cantidad de entradas que desea comprar: "))

MONTOTOTAL=1500*cantEntradas 


if metodoDePago==5:
    MONTOTOTAL=aplicarPuntos(MONTOTOTAL)


totalFinal=aplicarDescuento(MONTOTOTAL,metodoDePago)
print ("El precio final es: ", totalFinal)