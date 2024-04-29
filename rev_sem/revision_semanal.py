import os
## TODO: Hacer que exista una lista de funciones y por cada una el iniciar las llame y formatee con un espacio y espaciado final



class Jobs:


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
        print("-> Revisar los topicos activos del proyecto en gantt")
        print("-> Ajusta los tiempos necesarios")
        print("-> Incorpora o elimina topicos segun las necesidades de estudio en td para el proyecto")
        self.espaciado_final()
    
    def revision_emigracion(self):
        self.espaciado()
        print("Revision de plan Emigracion!")
        print("Revisar diagrama del plan y estimar la evolucion")
        print("Actualizar el estado tanto de las acciones/proyectos en Anyt como el diagrama")
        self.espaciado_final()
    
    def revision_algun_dia_tal_vez(self):
        self.espaciado()
        print("-> Lista los proyectos y determina cuales son activos activos...") 
        print("-> Lista incubables relacionados a esos proyectos")
        print("-> Ir determinando si hay que desincubar algo...")
        self.espaciado_final()

    def delegados(self):
        self.espaciado()
        print("Revisa lista de delegados y determina que hacer")
        print("No introduzcas en inbox, directamente a siguiente accion o calendario")
        self.espaciado_final()

    def recopilar(self):
        self.espaciado()
        print("Recopila TODO los inputs e ideas a tus bandejas de entrada")
        print("En caso de no poder recopilar algo, deja un recordatorio de ello en la bandeja")
        self.espaciado_final()

    def revisar_calendario(self):
        self.espaciado()
        print("-> Revisa tu calendario de la semana vivida")
        print("")
        print("-> Responde:")
        print("  Olvidaste algun compromiso?")
        print("  Algo no pudo hacerse y debe reprogramarse?")
        print("  Algo se tuvo que cancelar?")
        self.espaciado_final()
    
    def revisar_acciones_de_proyectos_mas_importantes(self):
        self.espaciado()
        print("Que acciones realice? Modificar el estado de las ya hechas o canceladas")
        print("Ahora mira los proyectos MAS importantes y...")
        print("Que acciones traban otras de gran impacto? Puedo priorizarlas de alguna manera?")
        self.espaciado_final()
    
    def actualizar_estado_de_bloqueo_de_acciones(self):
        self.espaciado()
        print("Por cada proyecto importante actualmente")
        print("Revisa que ACCIONES ya NO estan mas BLOQUEADAS e indicalo")
        print("Asi tambien actualiza el estado de las que ya terminaron")
        print("")
        print("Ahora tambien realizalo de la lista de acciones en general, las mas importantes")
        self.espaciado_final()
    
    def revisar_situacion_actual(self):
        self.espaciado()
        print("-> Determina los items importantes de SITUACION ACTUAL")
        print("")
        print("-> RESPONDE estas preguntas sobre los items importantes:")
        print("-  ¿Con que recursos cuento para la siguiente semana?")
        print("-  ¿Que recursos espero que crezcan esta semana? Que debo hacer para ello?")
        print("-  -> Abrir lista de projects importantes y responder")
        print("      ¿Deberia invertir algun recurso en algun proyecto o accion prioritaria?")
        self.espaciado_final()

    def actualizar_situacion_actual(self):
        self.espaciado()
        print("-> Abri el directorio de situacion actual con now")
        print("")
        print("-> Actualiza TODO del directorio de situacion actual")
        print("")
        print("Lista de fuentes de informacion de situacion actual")
        print("Social: Whatsapp, Agenda, Correo, Linkedin")
        print("Financiera: Banco patagonia homebanking, Santander homebanking, AirTM app, MercadoPago app, Banco Nacion App, Sube App")
        print("Conocimiento: Notas en papel, Zettelkasten")
        self.espaciado_final()

    def revisar_calendario_siguiente_semana(self):
        self.espaciado()
        print("Abri el calendario")
        print("Revisa la semana siguiente")
        print("")
        print("-> Buscar que compromisos voy a tener")
        print("-> Procesar: ¿Que deberia hacer para maximizar el exito de esos compromisos?")
        self.espaciado_final()

    def registro_revision(self):
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
