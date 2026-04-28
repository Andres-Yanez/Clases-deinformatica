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
            print("reprobado")
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












# %%
