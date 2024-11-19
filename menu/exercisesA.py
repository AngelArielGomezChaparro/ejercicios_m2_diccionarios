
from logica.exercisesA import save_course, search_currency


def designOneList():
    course = input("what is the course name?  ")
    result = save_course(course)
    print(result)

def designOneDict():
    currency = input("what is the currency name? ")
    print(search_currency(currency))














#Escribir un programa que almacene las asignaturas de un
#curso (por ejemplo Matemáticas, Física, Química, Historia
#y Lengua) en una lista y la muestre por pantalla.
# menu/display.py

#from logica.exercisesA import get_asignature

#def display_subjects():
    #subjects = get_asignature()
    #print("Asignaturas del curso:")
    #for subject in subjects:
    #    print(f"- {subject}")
