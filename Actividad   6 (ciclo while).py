clave = ""
while clave != "python123":
    clave = input("Ingrese la clave: ")
print("Acceso concedido")

#%%
opcion = ""
while opcion != "C":
    print("=== MENÚ ===")
    print("A. Saludar")
    print("B Mostrar mensaje")
    print("C Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == "A":
        print("Hola, bienvenido")
    elif opcion == "B":
        print("Estamos aprendiendo ciclos while")
    elif opcion == "C":
        print("Saliendo del programa")
    else:
        print("Opción invalida")

# %%

##
contraseña= ""
con = input("Ingrese la contraseña:")
while con != "python123":
    print("Acceso denegado")
else:
    print("Acceso permitido")    

## Ciclo for
numers=[0,1,2,3,4,5]
for numers in numers:
    print(numers)
#%%
notas = [8,7,9,10,6]
suma = 0
cantidad = 0
for nota in notas:
    suma = suma + nota
    cantidad = cantidad + 1
promedio = suma / cantidad
print(f"El promedio es: {promedio}")
# %%

palabra = input("Ingrese una palabra: ")
vocales = 0
consonantes = 0
total = 0
for letra in palabra:
    if letra != " ":
        total = total + 1
        letra = letra.lower()
        if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
            vocales = vocales + 1
        else:
            consonantes = consonantes + 1
print("Total:", total)
print("Vocales:", vocales)
print("Consonantes:", consonantes)

#%%
it_companies = {"Facebook","Facebook" "Google", "Apple", "Amazon"}
for company in it_companies:
    print(company)
#%%
asistentes = {'Ana', 'Luis', 'María', 'Ana', 'Carlos', 'Luis', 'Sofía'}
for estudiante in asistentes:
    print('Generar certificado para:', estudiante)

#%%
lista=[1,2,3,4,5]
numbers = input("Ingrese un numero: ")
for number in lista:
    if number == 3 :
        print("Numero encontrado")
        break
else:
    print("Numero no encontrado")    
# %%
cedula = input("Ingrese su numero de cedula: ")
cedula_limpia = ""
for caracter in cedula:
    if caracter == '-' or caracter ==  "":
        continue
    cedula_limpia = cedula_limpia + caracter
print(cedula_limpia)