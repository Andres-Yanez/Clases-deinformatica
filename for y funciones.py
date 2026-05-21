for numero in range(5):
    print(numero)
##
for numero in range(2, 7):
    print(numero)
##
for numero in range(1, 10, 2):
    print(numero)
##
for numero in range(10, 0, -2):
    print(numero)
##
for fila in range(3):
    for columna in range(4):
        print("*", end=" ")
    print()
##
for numero in range(5):
    print(numero)
else:
    print("El ciclo terminó correctamente")
##
for numero in range(5):
    if numero == 3:
        break
    print(numero)
else:
    print("El ciclo terminó correctamente")
##
for numero in range(5):
    if numero == 3:
        pass
    print(numero)


suma = 0
cantidad = int(input("Ingrese la cantidad de notas: "))
if cantidad < 2:
    print("No es posible calcular el promedio con menos de 2 notas.")
else:
    contador = 0
    while True:
        nota = float(input(f"Ingrese la nota {contador}: "))
        suma += nota
        contador += 1
        if contador == cantidad:
            break
    promedio = suma / cantidad
    print(f"El promedio es: {promedio}")

#tabla de multiplicar
numero = int(input("Ingrese un número: "))
inferior= int(input("Desde que numero desea ver: "))
superior= int(input("Hasta que numero desea ver: "))
for i in range(inferior, superior + 1 ):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

#promedio
notas = [5, 8, 9, 7, 10]
suma=0
cantidad=0
for i in range(1,4):
    suma= suma + notas [i]
    cantidad= cantidad + 1
promedio= suma/ cantidad
print("Promedio de notas parciales:",{promedio})

#tabla de multiplicar
numero = int(input("Ingrese un número: "))
for i in range(9,1,-2):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
# Asignar estudiantes a los puestos de un laboratorio
# El laboratorio tiene 3 filas y 4 computadoras por cada fila
# Ciclo externo: recorre las filas del laboratorio
# range(1, 4) genera los valores 1, 2 y 3
for fila in range(1, 4):
    # Ciclo interno: recorre las computadoras de cada fila
    # range(1, 5) genera los valores 1, 2, 3 y 4
    for computadora in range(1, 5):
        # Solicita el nombre del estudiante que será asignado al puesto actual
        nombre = input("Ingrese el nombre del estudiante: ")
        # Muestra el nombre del estudiante y el puesto asignado
        print(f"{nombre} asignado a Fila {fila} - Computadora {computadora}")
    # Este mensaje se muestra cuando termina la asignación de una fila completa
    print(f"Fin de la fila {fila}")