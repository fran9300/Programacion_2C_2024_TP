
from entities.movies import getMovies,addMovie
from numeration import getSecuences 
from entities.user import getUsers,addUser

lastMenu = {}
currentMenu = {}
# TODAS LAS "ENTIDADES" EN SU PRIMER CAMPO TIENE EL ID
    # [
    #     [id,nombre,duracion],
    #     [id,nombre,duracion],
    #     [id,nombre,duracion],
    # ]



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


valorEntrada = 2000

def getValorEntrada():
    return valorEntrada

def setValorEntrada(number):
    global valorEntrada
    valorEntrada = number



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
    addMovie()
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
    addUser()
    return None

def configDescuentoPorTipoDePago(metodosID):
    
    descuentos = {
        1: 0.30,  # Cash: 30% descuento
        2: 0.20,  # Transfer: 20% descuento
        3: 0.10,  # Debt: 15% descuento
        4: 0.02,  # Credit: 10% descuento
        #Points lo hago en funcion aparte
    }
    
    if metodosID in descuentos:
        return descuentos[metodosID] #Devuelve el descuento que hay que aplicar
                                    #Por ej: el metodoID es 1, entonces devuelve 0.30
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
    total = getValorEntrada() * cantidadEntradas
    return total

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
        valorFinal=total-(total*descuento)
        return valorFinal

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
    MetodosDePago = [
        [1, "Cash"],
        [2, "Transfer"],
        [3, "Debt"],
        [4, "Credit"],
        [5, "Points"]
    ]
    
    while True:
        print("Opciones de método de pago:")
        for metodo in MetodosDePago:
            print(metodo[0], metodo[1])
        
        opcion = input("Ingrese el número del método de pago: ")
        
        if opcion.isdigit():  # Verifica si opcion es un número
            opcion = int(opcion) #Transpforma opcion en entero por si el usuaario lo ingreso mal 
           
            for metodo in MetodosDePago:
                if metodo[0] == opcion:
                    return metodo[0]
                
            print ("El numero ingresado no es valido. Ingrese otro numero")
            
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

def clientManage():
    consultarPeliculas()
    comprarEntrada()
    configuracionDelUsuario()
    return ''

def imprimirMenu(menu):
    print("Ingrese el punto de menu")
    for key in menu.keys():
        print(f"{key}-{menu[key].__name__}")
def initAdminMenu():
    return mainMenuAdmin
def initClientMenu():
    return None #tiene que devolver el menu de usuario

def GestionPeliculas():
    global lastMenu
    global currentMenu
    lastMenu = currentMenu
    currentMenu  = gestionPeliculas
    getSubMenu(gestionPeliculas)




#Programa principal
# metodoDePago=pedirMetodoDePago()
# print ("Metodo de pago seleccionado:", metodoDePago)

# cantEntradas=int(input("Ingrese la cantidad de entradas que desea comprar: "))

# montoTotal=calcularTotal(5)


# if MetodosDePago==5:
#     montoTotal=aplicarPuntos(montoTotal)


# totalFinal=aplicarDescuento(montoTotal,MetodosDePago)
# print ("El precio final es: ", totalFinal)

def getSubMenu(subMenu):
    imprimirMenu(subMenu)
    menuValue = ''
    while(menuValue != 'exit'):
        menuValue = input()
        if(menuValue in subMenu.keys()):
            subMenu[menuValue]()
            imprimirMenu(subMenu)
        elif menuValue != 'exit':
            print("El valor ingresado no existe en el menu, vuela a ingresar" )

def getParentMenu():
    global currentMenu
    getSubMenu(lastMenu)
    currentMenu = lastMenu
#Esto deberia ir en un archivo que sea menu. Y cada funcion por tipo deberia ir en su propio archivo asi no ahcemos import circular
gestionPeliculas = {
    "0":consultarPeliculas,
    "1":cargarPelicula,
    "2":eliminarPelicula,
    "3":getParentMenu
}
mainMenuAdmin = {
    "1":GestionPeliculas,
    "2":cargarSala,
    "3":asignarPeliculaASala,
    "4":configDescuentoPorTipoDePago,
    "5":liberarSala,
    "6":register
}
# print("ejemplo getById")
# print(getById(2,getMovies()))      


login = int(input("0 es admin, 1 es usuario"))
if(login == 0):
    currentMenu
    mainMenu = initAdminMenu()
    currentMenu = mainMenu
    getSubMenu(mainMenu)
