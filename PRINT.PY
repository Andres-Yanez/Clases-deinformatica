#Actividad 1
"""Andres Yanez 
proyecto 1 
9/04/2026"""
print(type("120"))
print(type(120.05))
print(type(120))
print(7%4)
print(7//4)



# ===== PARTE A ===== 

# Respuesta 1:
# a) Tipos de datos:
# nombre -> str (cadena de texto)
# edad -> int (entero)
# promedio -> float (decimal)
# materias -> list (lista)

# b) Salida en pantalla:
# <class 'str'>
# <class 'int'>
# <class 'float'>
# <class 'list'>
# 5

# c) len(nombre) devuelve la cantidad de caracteres del texto "Mateo", que es 5.


# Respuesta 2:
# a) Diferencia:
# Guardar un valor en una variable significa almacenarlo en memoria,
# mientras que print() solo muestra ese valor en pantalla.

# b) Porque input() siempre devuelve datos tipo string (texto),
# incluso si el usuario escribe números.

# c) Diferencias:
# **  -> potencia (ej: 2**3 = 8)
# //  -> división entera (ej: 7//3 = 2)
# %   -> residuo o módulo (ej: 7%3 = 1)

# e) Instrucción:
import keyword
print(keyword.kwlist)



# ===== PARTE B ===== 

# Código corregido

base = float(input("Ingrese la base del anuncio: "))
altura = float(input("Ingrese la altura del anuncio: "))
precio = float(input("Ingrese el precio por metro cuadrado: "))

superficie = base * altura
valor = superficie * precio

print("Superficie total:", superficie)
print("Valor estimado:", valor)

# Respuestas:
# a) Errores principales:
# - input() devuelve texto, no números
# - No se podía multiplicar strings
# - Se intentaba concatenar texto con números

# b) Funciona porque:
# - Se convierten los datos a float
# - Ahora sí se pueden hacer operaciones matemáticas
# - Se usa print correctamente con valores numéricos



# Construcción breve

frase = "Aprender Python es útil"

print(frase.lower())
print(len(frase))
print("Python" in frase)
print(frase.replace("útil", "interesante"))
print(frase.split())



# ===== PARTE C ===== 

# Programa integrador

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
pais = input("Ingrese su país: ")
ancho = float(input("Ingrese el ancho de la vitrina: "))
alto = float(input("Ingrese el alto de la vitrina: "))
precio = float(input("Ingrese el precio por metro cuadrado: "))

area = ancho * alto
costo_total = area * precio

nombre_completo = nombre + " " + apellido

print(f"\n--- REPORTE FINAL ---")
print(f"Nombre completo: {nombre_completo}")
print(f"País: {pais}")
print(f"Área: {area}")
print(f"Costo total: {costo_total}")

print(f"Nombre en mayúsculas: {nombre_completo.upper()}")
print(f"Longitud del nombre: {len(nombre_completo)}")
print(f"¿Contiene la letra 'a'?: {'a' in nombre_completo.lower()}")
print(f"¿El costo es mayor a 100?: {costo_total > 100}")