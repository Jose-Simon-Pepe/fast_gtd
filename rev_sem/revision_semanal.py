import os
from system import system
## TODO: Hacer que exista una lista de funciones y por cada una el iniciar las llame y formatee con un espacio y espaciado final



class Jobs:

    def __init__(self,system=None):
        self._system=system

    def espaciado(self):
        os.system("clear")  
        print("#=======================================#")
        print("")

    def espaciado_final(self):
        print("")
        print("-----------------------------------------")

    def revision_estudio(self):
        self.espaciado()
        print("-> Abrir Gantt de estudio")
        #TODO: Action: abrir archivo de gantt estudio pdf y herramienta de gantt online
        print("-> Revisar los topicos activos del proyecto en gantt")
        #TODO: Action: Abrir lista de necesidades de estudio en situacion actual
        print("-> Ajusta los tiempos necesarios")
        print("-> Incorpora o elimina topicos segun las necesidades de estudio en td para el proyecto")
        #TODO: Action: Abrir lista de necesidades de estudio en situacion actual
        self.espaciado_final()
    
    def revision_emigracion(self):
        self.espaciado()
        print("Revision de plan Emigracion!")
        #TODO: Action: Abrir el archivo de plan inmigracion en excalidraw local (intentar hacer que se abra cargando el archivo automaticamente)
        print("Revisar diagrama del plan y estimar la evolucion")
        print("Actualizar el estado tanto de las acciones/proyectos como el diagrama")
        #TODO: ACTION: Listar acciones por proyecto activo
        self.espaciado_final()
    
    def revision_algun_dia_tal_vez(self):
        self.espaciado()
        print("-> Lista los proyectos y determina cuales son activos activos...") 
        #TODO: action: listar proyectos
        #TODO Permitir al usuario seleccionar en algun lugar los proyectos activos
        print("-> Lista incubables relacionados a esos proyectos")
        #TODO: abrir instancia en tmux con el comando now una vez por cada proyecto marcado como activo
        print("-> Ir determinando si hay que desincubar algo...")
        self.espaciado_final()

    def delegados(self):
        self.espaciado()
        print("Revisa lista de delegados y determina que hacer")
        #TODO: action: Abrir lista de delegados
        print("No introduzcas en inbox, directamente a siguiente accion o calendario")
        #TODO: abrir calendario calcurse
        #TODO: Abrir $HOME con el comando TD ADD de manera iterativa
        self.espaciado_final()

    def recopilar(self):
        self.espaciado()
        print("Recopila TODO los inputs e ideas a tus bandejas de entrada")
        print("En caso de no poder recopilar algo, deja un recordatorio de ello en la bandeja")
        #TODO: ACTION: Abrir fuentes de informacion digitales una por vez
        #TODO: ACTION: Abrir el directorio de "input" con el comando TD ADD de manera iteractiva
        self.espaciado_final()

    def revisar_calendario(self):
        self.espaciado()
        print("-> Revisa tu calendario de la semana vivida")
        #TODO: ACTION: Abrir calcurse posicionado a comienzo de semana
        print("")
        print("-> Responde:")
        #TODO: Por cada dia, iniciar calcurse posicionado en ese dia y responder, por cada dia, estas siguintes 3 preguntas de manera iterativa
        print("  Olvidaste algun compromiso?")
        print("  Algo no pudo hacerse y debe reprogramarse?")
        print("  Algo se tuvo que cancelar?")
        self.espaciado_final()
    
    def revisar_acciones_de_proyectos_mas_importantes(self):
        self.espaciado()
        print("Que acciones realice? Modificar el estado de las ya hechas o canceladas")
        #TODO: ACCION: Listar acciones por proyecto de manera interactiva una lista de acciones por vez|
        print("Ahora mira los proyectos MAS importantes y...")
        #TODO: ACCION: Listar acciones por proyecto de manera interactiva una lista de acciones por vez|
        print("Que acciones traban otras de gran impacto? Puedo priorizarlas de alguna manera?")
        #TODO: ACCION: Listar acciones por proyecto de manera interactiva una lista de acciones por vez|
        self.espaciado_final()
    
    def actualizar_estado_de_bloqueo_de_acciones(self):
        self.espaciado()
        print("Por cada proyecto importante actualmente")
        print("Revisa que ACCIONES ya NO estan mas BLOQUEADAS e indicalo")
        #TODO: ACCION: listar proyectos
        #TODO: ACCION: listar acciones por cada proyecto de manera interactiva 1 c/vez
        #TODO: ACCION: Pausa
        print("Asi tambien actualiza el estado de las que ya terminaron")
        #TODO: ACCION: listar proyectos
        #TODO: ACCION: listar acciones por cada proyecto de manera interactiva 1 c/vez
        #TODO: ACCION: Pausa
        print("")
        print("Ahora tambien realizalo de la lista de acciones en general, las mas importantes")
        #TODO: ACCION: listar proyectos
        #TODO: ACCION: listar acciones por cada proyecto de manera interactiva 1 c/vez
        #TODO: ACCION: Pausa
        self.espaciado_final()
    
    def revisar_situacion_actual(self):
        self.espaciado()
        print("-> Determina los items importantes de SITUACION ACTUAL")
        #TODO: Listar items SIN REPETICION de situacion actual
        #TODO: ACCION: Permitir escojer los items de situacion actual a usar
        #TODO: ACCION: Pausa
        print("-> RESPONDE estas preguntas sobre los items importantes:")
        #TODO: ACCION: Por cada pregunta abrir la lista de recursos
        #TODO: ACCION: Por cada pregunta pedir y registrar respuesta de usuario
        print("-  ¿Con que recursos cuento para la siguiente semana?")
        #TODO: ACCION: Abrir calendario de la siguiente semana
        print("-  ¿Que recursos espero que crezcan esta semana? Que debo hacer para ello?")
        print("-  -> Abrir lista de projects importantes y responder")
        #TODO: action: Abrir lista de proyectos
        print("      ¿Deberia invertir algun recurso en algun proyecto o accion prioritaria?")
        self.espaciado_final()

    def actualizar_situacion_actual(self):
        self.espaciado()
        #TODO: ACTION: por cada lista de fuente de informacion actual listar una a una y realizar las actions siguientes
        #TODO: Action: Abrir el directorio de situacion actual usando now
        print("-> Abri el directorio de situacion actual con now")
        print("")
        print("-> Actualiza TODO del directorio de situacion actual")
        #TODO: ACTION Por cada elemento de now, sin repeticion, listar el td, de maera iterativa una por vez
        print("")
        print("Lista de fuentes de informacion de situacion actual")
        print("Social: Whatsapp, Agenda, Correo, Linkedin")
        print("Financiera: Banco patagonia homebanking, Santander homebanking, AirTM app, MercadoPago app, Banco Nacion App, Sube App")
        print("SERVICIOS de casas: www.naturgy.com.ar, edenordigital.com:Edenor1Lola y Aysa solo va por correo")
        print("Conocimiento: Notas en papel, Zettelkasten")
        self.espaciado_final()

    def revisar_calendario_siguiente_semana(self):
        self.espaciado()
        print("Abri el calendario")
        self._system.open_cal()
        print("Revisa la semana siguiente")
        print("")
        print("-> Buscar que compromisos voy a tener")
        print("-> Procesar: ¿Que deberia hacer para maximizar el exito de esos compromisos?")
        self.esperar()
        self._system.close_cal()

    def registro_revision(self):
        #TODO: El registro puede hacerse digitalmente de manera programatica siguiendo las respuestas del usuario, hacerlo de manera programatica
        self.espaciado()
        print("Considerando el valor de impacto de los objetivos de medio plazo")
        print("")
        print("-> Abra el registro de revisiones en ~/registro_revisiones/revisiones.md")
        print("-> Liste todos sus proyectos activos")
        print("-> Primero: Vuelque los asuntos a resolver en la revision")
        print("-> Mientras revisa: Vaya registrando accionables en el documento, luego los eliminara de ahi")
        print("-> Mientras revisa: USE DOCUMENTACION del proyecto en trabajo (~/nombre_de_proyecto/general.adoc)")
        print("-> Luego: Dediquese a realizar este checklist siguiente.")
        print("-> Al finalizar, vuelque tanto las decisiones tomadas como el metodo elegido para cada una")
        print("")
        print("- Dado que para el proceso de planificacion se usan herramientas como excalidraw,")
        print("-> debe volcar esos archivos con un nombre apropiado")
        self.espaciado_final()

    def esperar(self):
        input("Terminaste? s")

def fin_revision_futuro():
    j= Jobs()
    print("Lo lograste! Revision semanal futuro completada")
    os.system("clear")
    print("Ahora, vuelque tanto las decisiones tomadas como el metodo elegido para cada una.")
    j.esperar()

def run_short_future_revision():
    j= Jobs()
    j.registro_revision()
    j.esperar()
    j.revisar_calendario()
    j.esperar()
    j.revisar_calendario_siguiente_semana()
    j.esperar()
    fin_revision_futuro()

def run_long_future_revision():
    j= Jobs()
    j.registro_revision()
    j.esperar()
    j.revisar_calendario()
    j.esperar()
    j.revisar_calendario_siguiente_semana()
    j.esperar()
    j.revisar_situacion_actual()
    j.esperar()
    j.revision_algun_dia_tal_vez()
    j.esperar()
    j.revision_estudio()
    j.esperar()
    fin_revision_futuro()


def run_past_revision():
    j= Jobs()
    j.actualizar_estado_de_bloqueo_de_acciones()
    j.esperar()
    j.revisar_acciones_de_proyectos_mas_importantes()
    j.esperar()
    j.delegados()
    j.esperar()
    j.recopilar()
    j.esperar()
    j.actualizar_situacion_actual()
    j.esperar()
    print("Lo lograste! Revision semanal pasado completada")

#TODO: Las acciones DEBEN ser efectuadas en una instancia de terminal una separada de otra, usando tmux para multiplexarla
#TODO: Al iniciar cualquier tipo de revision, asegurarme que la revision se esta ejecutando en una instancia de tmux, si no, debe iniciarse tmux y correr esa revision
#TODO: Hacer que cada respuesta del usuario sea registrada automaticamente en el registro de revision semanal correspondiente.
