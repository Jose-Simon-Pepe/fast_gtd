# Flujo de prints con el flujo de gtd
def organizar_accion_depende_de_mi(accion):
    print("Entonces "+accion+"...")
    print("1. Bloqueada")
    print("2. Siguiente")
    posible = input("es accion siguiente o esta bloqueada? ")
    if posible.lower() == "1":
        print("Indicar que accion o proyecto la bloquea")
        print("Poner en lista de acciones bloqueadas")
        print("Terminaste con "+accion)
    if posible.lower() == "2":
        print("Complete atributos de la accion "+accion)
        tiempo = input("Indica el tiempo a dedicar")
        contexto = input("Indica en que contexto es accionable")
        energia = input("Indica cuanta energia requiere")
        print("")
        print("Genial!")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("Ahora debes ingresar en AnyType siguiente")
        print("")
        print("Para accion: "+accion)
        print("tiempo dedicable= "+tiempo+"| contexto accionable= "+contexto+"| energia requerida= "+energia)
        print("Ademas debes indicar el/los OBJETIVO/S que impacta")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

def delegar(accion):
    print("Entonces, sobre "+accion)
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("Debes registrar en AnyType lo siguiente:")
    print("")
    print("Registrar en delegados PERSONA y accion "+accion)
    print("En caso de ser necesario, CALENDARIZA un recordatorio")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")


def flujo_organizar_acciones(accion):
    print("")
    print("Organizando accion: "+accion)
    print("")
    depende = input("depende de mi? (y/n) ")
    if depende.lower() == 'y':
        organizar_accion_depende_de_mi(accion)
    if depende.lower() == 'n':
        delegar(accion)

def flujo_planificar_proyecto(lista_acciones):
    print("Vas a planificar un proyecto o mas para estas acciones:")
    for accion in lista_acciones:
        print(accion)
    proyectos = input("En que proyecto/s se agrupan las acciones?")
    print("")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("Debes registrar en AnyType lo siguiente:")
    print("")
    print("Nuevo proyecto/s: "+proyectos)
    print("Ademas debes indicar el/los OBJETIVO/S que impacta")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("Muy bien!!")
    print("")
    print("Ahora organizaras cada accion del/os proyecto/s "+proyectos)
    for accion in lista_acciones:
        flujo_organizar_acciones(accion)
    print("Terminaste con la organizacion de acciones de los proyectos.")

def decidir():
    return input("Decida una accion concreta, deje en blanco para terminar")

def obtener_lista_acciones(tarea):
    lista = list()
    print("Ahora vamos a planificar como conseguir exitosamente el objetivo")
    print("Estamos trabajando sobre tarea: "+tarea)
    print("")
    accion = decidir()
    while accion.rstrip():
        lista.append(accion)
        accion = decidir()
    return lista



def flujo_procesar_accionable():
    print("Consultando mis recursos y situacion actual...")
    tarea = input("Que creo que debo hacer? ")
    print("")
    print("Pensemos sobre como hacer "+tarea)
    print("")
    print("1. Solo una accion")
    print("2. Muchas acciones")
    cuantas_acciones = input("Cuantas acciones atomicas componen a esa tarea? ")
    if cuantas_acciones == '2':
        lista_acciones = obtener_lista_acciones(tarea)
        flujo_planificar_proyecto(lista_acciones)
    if cuantas_acciones == '1':
        accion_unica = input("Defina la accion")
        flujo_organizar_acciones(accion_unica)




def flujo_procesar_no_accionable():
    print("1. Tirar")
    print("2. Algun dia/tal vez")
    print("3. Referencia de proyecto")
    no_acci = input("Que deberia hacer?")
    if no_acci == '1':
        print("Tiralo!")
    if no_acci == '2':
        tipo_lista = input("Afecta a algun proyecto activo o a objetivos medio plazo?")
        print("Bien")
        afectado = input("Escribi que proyecto u objetivo sera afectado")
        print(r"Envialo a "+tipo_lista+" (subcarpeta de Algun dia Tal vez ) con el nombre: quiza_afecte_a_"+afectado)
    if no_acci == '3':
        print("Adjuntalo en el objeto del proyecto/s impactado/s en AnyType y explica alli como impacta.")

def start():
    print("Inicia el proceso")
    significado = input("Que significa para mi? ")
    print("")
    print("Significado:")
    print(significado)
    print("")
    accionable = input("Es accionable? (y/n)")
    if accionable.lower().__eq__("y"):
        flujo_procesar_accionable()
    else:
        flujo_procesar_no_accionable()


while True:
    start()
