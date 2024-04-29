import os
from rev_sem.revision_semanal import run_past_revision

def espaciado():
    os.system("clear")  
    print("#=======================================#")
    print("")


def espaciado_final():
    input("Terminado? >")
    print("")
    print("-----------------------------------------")

def step(func):
    def wrapper():
        espaciado()
        func()
        espaciado_final()
    return wrapper

@step
def agrupar_inputs_relacionados():
    print("Revisando los inputs de maxima prioridad digitales")
    print("Agrupalos segun el tema")
    print("Por ejemplo, los inputs de necesidades de estudio van en /estudio")

@step
def filtrar_inputs_prioritarios():
    print("Revisa la bandeja de entrada FISICA y DIGITAL RAPIDO y determina si...")
    print("Eliminar un input (no tiene valor ni potencial)")
    print("Priorizar al maximo un input (porque impacta fuertemente a objetivos mas importantes)")
    print("A lo que elijas priorizar, debes separarlo en un apartado")
    print("")
    print("No olvide de filtrar la bandeja fisica")

@step
def procesar_inputs():
    print("Abri el apartado de inputs priorizados")
    print("Ejecuta el script de procesamiento de inputs")
    print("No termines la sesion hasta haberlo procesado todo")

run_past_revision()
filtrar_inputs_prioritarios()
agrupar_inputs_relacionados()
procesar_inputs()
