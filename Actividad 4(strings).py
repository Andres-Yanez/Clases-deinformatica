strings_varias_lineas= """
Andres Yanez
informatica
"""
print(strings_varias_lineas)
colegio= "ISM"
longitud = len(colegio)
print(longitud)
print(len("San Francisco De Quito"))
nombre= "Andres"
apellido= "Yanez"
nombre_completo= nombre + " " + apellido
print(nombre_completo)
print("Mi nombre completo es: ", nombre_completo)
print(nombre_completo*3)
print("Python\nChallenge")
print("Days\tTopics")
print("Simbolo(\\)")
print(f"Mi nombre es: {nombre} y mi apellido es: {apellido}")
#%%
language= "Python"
a,b, c, d, e, f= language
print(language[2])
print(language[-1])
print(language[0:3])
ultimas_letras= language[-3:]
print(ultimas_letras)
#%%
gretting = "Dia martes en clase de informatica"
print(gretting[::-1])
#%%
language= "Python"
print(language[2:6:2])
#%%
challenge= "thirty Days Of Python"
print(challenge.capitalize())
