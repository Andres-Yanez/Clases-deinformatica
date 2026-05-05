a=3
if a > 0:
    print(f"{a} is a positive number")
else: 
    print(f"{a} is a negative number")
print("Gracias por usar el programa")
#%%
calificacion = float(input("Ingrese su calificación: "))
if calificacion >= 90:
    print("A")
else:
    if calificacion >= 80:
        print("B")
    else:
        if calificacion >= 70:
            print("C")
        else:
            print("F")
#%%                  
numero = int(input("Ingrese un número: "))
if numero > 0 and numero % 2 == 0:
    print(f"{numero} es un número par positivo")
elif numero > 0 and numero % 2 == 1:
    print(f"{numero} es un número impar positivo")
elif numero < 0 and numero % 2 == 0:
    print(f"{numero} es un número par negativo")
elif numero < 0 and numero % 2 == 1:
    print(f"{numero} es un número impar negativo")
else: 
    print("el número es cero")
#%%
"""numero = int(input("Ingrese un número: "))
if numero == 0:
    print("el número es cero")
else:
    if numero > 0:
        if numero % 2 == 0:
            print(f"{numero} es un número par positivo")
        else:
            print(f"{numero} es un número impar positivo")
    else:
            if numero % 2 == 0:
                print(f"{numero} es un número par negativo")
            else:
                print(f"{numero} es un número impar negativo")
print("Gracias por usar el programa")"""                

#%%
#shorthand
numero = int(input("Ingrese un número: "))
print(f"{numero} es positivo y par ") if numero > 0 and numero % 2 == 0 else print(f"{numero} es positivo e impar") if numero > 0 and numero % 2 == 1 else print(f"{numero} es negativo y par") if numero < 0 and numero % 2 == 0 else print(f"{numero} es negativo e impar") if numero < 0 and numero % 2 == 1 else print(f"{numero} es cero")

#Tarea
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Tienes la edad suficiente para aprender a conducir")
else:
    faltan = 18 - edad
    print(f"Te faltan {faltan} años para aprender a conducir")
#%%
mi_edad= 17
su_edad = int(input("Ingrese su edad: "))
if su_edad >= mi_edad:
    faltan = su_edad - mi_edad
    print(f"Eres mayor o igual que yo, que tengo {mi_edad} años")
else:
    print(f"Eres menor que yo, te faltan {faltan} años")

# %%
calificacion = float(input("Ingrese su calificación: "))
if calificacion >= 90:
    print("A")
else:
    if calificacion >= 80:
        print("B")
    else:
        if calificacion >= 70:
            print("C")
        else:
            print("F")
#%%
mes = input("Ingrese el mes: ")
if mes == "Septiembre" or mes == "Octubre" or mes == "Noviembre":
    print("El mes es de otoño")
else:
    if mes == "Diciembre" or mes == "Enero" or mes == "Febrero":
        print("El mes es de invierno")
    else:
        if mes == "Marzo" or mes == "Abril" or mes == "Mayo":
            print("El mes es de primavera")
        else:
            if mes == "Junio" or mes == "Julio" or mes == "Agosto":
                print("El mes es de verano")
            else:
                print("Mes no válido")
#%%
#              