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
