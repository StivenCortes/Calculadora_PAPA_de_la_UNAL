"""
Vamos a crear un programa que nos permita calcular el PAPA de un estudiante,
Para ello se debe solicitar al usuario la siguiente información:
- Número de asignaturas a calcular.
- Nombre de la asignatura.
- Nota obtenida en la asignatura.
- Creditos de la asignatura.

¿Que es el PAPA?, el PAPA es el Promedio Aritmético Ponderado Acomulado,
puedes entenderlo como el promedio de un estudiante durante toda su carrera. El cual se calcula de la siguiente manera:
PAPA = (Nota1 * Creditos1 + nota2 * Creditos2 + ... + Notan * Creditosn) / (Creditos1 + Creditos2 + ... + Creditosn)
"""

print("Bienvenido al programa para calcular el PAPA\n")
numero_asignaturas = int(input("Por favor, ingrese el número de asignaturas cursadas: "))

# Como son varias asignaturas, vamos a crear una lista
asignaturas = []
contador = 0

while True:
    contador += 1

    print(f"Materia número {contador} ")
    print("Ingrese los siguientes datos nombre de la asignatura, nota de la asignatura, numero de creditos.")
    print("Ejemplo: Matematicas, 5, 4\n")


    if contador >= numero_asignaturas:
        break