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

##
numero = int(input("Ingrese un número: "))

for i in range(1, 11):
    resultado = numero * i
    print(numero, "x", i, "=", resultado)



suma= 0
for number in range(5):
    nota= float(input("Ingrese la nota: "))
    suma= suma + nota
promedio= suma / 5
print(f"El promedio es: {promedio}")