"""
Vamos a crear un programa que calcule el PAPA de un estudiante, 
para ello se debe solicitar al usuario la siguiente información:
- Número de materias cursadas
- Nombre de la asignatura
- Nota obtenida en la asignatura
- Número de créditos de la asignatura

Antes de continuar, se debe conocer que es el PAPA, el cual es el Promedio Aritmético Ponderado para Inscripciones,
puedes entenderlo como el promedio que tiene un estudiante durante el periodo académico, el cual se calcula de la siguiente manera:
PAPA = (Nota1 * Creditos1 + nota2 * Creditos2 + ... + Notan * Creditosn) / (Creditos1 + Creditos2 + ... + Creditosn)

Este promedio es muy importante ya que la Universidad Nacional de Colombia lo usa para decidir que estudiantes inscriben primero que los demas.
"""

print("Bienvenido este programa va a calcular tu PAPA.\n")

# Como son varias asignaturas, entonces las pondremos en una lista vacia
materias = []

# Se solicita al usuario el numero de materias cursadas y se inicializa un contador
numero_materias = int(input("Por favor, ingrese el numero de materias cursadas: "))
contador = 0

# Se solicita al usuario el nombre, nota y creditos de cada materia para poder almacenarlo en un diccionario
while True:
    # Se incrementa el contador de materias
    contador += 1
    
    # Se solicita al usuario el nombre, nota y creditos de la materia
    print(f"\nMateria número {contador}.")
    nombre_materia = input("Ingrese el nombre de la asignatura: ")
    nota_materia = float(input("Ingrese la nota de la asignatura: "))
    creditos_materia = int(input("Ingrese los créditos de la asignatura: "))
    print(" ")

    # Se crea un diccionario con la información de la materia
    materia = {
        "nombre": nombre_materia,
        "nota": nota_materia,
        "creditos": creditos_materia
    }

    # Se agrega el diccionario de la materia a la lista de materias
    materias.append(materia)

    # Creamos una condición para salir del bucle cuando se hayan ingresado todas las materias
    if contador >= numero_materias:
        break

# Se calculo los puntos y creditos totales
puntos_total = 0
creditos_total = 0
for materia in materias:
    puntos_total += materia["nota"] * materia["creditos"]
    creditos_total += materia["creidtos"]

# Calculamos el PAPA y lo redondeamos a 2 decimales
Nota_final = puntos_total / creditos_total
PAPA = round(Nota_final, 2)

# Informamos al usuario los resultados obtenidos
print(f"Los créditos cursados durante este semestre son {creditos_total}.")
print(f"El PAPA obtenido hasta el momento es {PAPA}.")
