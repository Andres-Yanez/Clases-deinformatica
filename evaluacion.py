# ===== PARTE A =====
# Respuesta 1:
#a) Indica el tipo de dato de cada variable
# nombre -> str 
# edad -> int 
# promedio -> float 
# materias -> list 
#b) Escribe qué mostraría el programa en pantalla
# <class "str">
# <class "int">
# <class "float">
# <class "list">
#5
#c) Explica qué hace len(nombre)
#La funcion len() devuelve la cantidad de caracteres que tiene el texto almacenado en una variable.
# Respuesta 2:
#a) ¿Qué diferencia hay entre almacenar un valor en una variable y mostrarlo con print()?
#Almacenar un valor en una variable es guardar ese valor en la memoria del programa, mientras que print() es una función que muestra ese valor en la pantalla.
#b) ¿Por qué input() devuelve texto aunque el usuario escriba un número?
#Porque la función input() siempre devuelve una cadena de texto, si el usuario escribe un numero automaticamnete se convierte en cadena de texto.
#c) Explica la diferencia entre los operadores **, // y %
#** es el operador de potencia, // es el operador de división entera solo toma la parte entera aunque exista decimal y % es el operador de residuo o módulo.
#e) Escribe una instrucción para mostrar en pantalla la lista de palabras reservadas de Python.
import keyword
# ===== PARTE B =====
#%%
base = float(input("Ingrese la base del anuncio: "))
altura = float(input("Ingrese la altura del anuncio: "))
precio = float(input("Ingrese el precio por metro cuadrado: "))
superficie = base * altura
valor = superficie * precio
print("Superficie total: " , superficie)
print("Valor estimado: ", valor)
#a) ¿Cuáles eran los errores principales?
# El error principal era que se estaba usando input() sin declararlos los valores a números.
#b) ¿Por qué la corrección funciona?
# La corrección funciona porque se convierten los valores ingresados por el usuario a números flotantes.
# Construcción breve
#%%
frase= "Aprender Python es util"
print(frase.lower())
print(len(frase))
print("Python" in frase)
print(frase.replace("util", "interesante"))
print(frase.split())
# PARTE C 
# Programa integrador
# %%
nombre = input("Ingrese su nombre:")
apellido = input("Ingrese su apellido:")
pais = input("Ingrese su país:")
ancho = float(input("Ingrese el ancho de la vitrina:"))
alto = float(input("Ingrese el alto de la vitrina:"))
precio = float(input("Ingrese el precio por metro cuadrado:"))
area = ancho * alto
costo_total = area * precio
nombre_completo = nombre + " " + apellido
print(f"REPORTE FINAL")
print(f"Nombre completo: {nombre_completo}")
print(f"País: {pais}")
print(f"Área: {area}")
print(f"Costo total: {costo_total}")
print(f"Nombre en mayúsculas: {nombre_completo.upper()}")
print(f"Longitud del nombre: {len(nombre_completo)}")
print(f"¿Contiene la letra 'a'?: {"a" in nombre_completo}")
print(f"¿El costo es mayor a 100?: {costo_total > 100}")
#22/04/2026