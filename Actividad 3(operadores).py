#Operadores
#%%
edad= type(int(17))
estatura= type(float(1.70))
#%%
base= input("Ingrese la base del triangulo: ")
altura= input("Ingrese la altura del triangulo: ")
area= 0.5*float(base)*float(altura)
print("El area del triangulo es: ", area)
#%%
lado1= input("Ingrese el lado 1 del triangulo: ")
lado2= input("Ingrese el lado 2 del triangulo: ")
lado3= input("Ingrese el lado 3 del triangulo: ")
perimetro= float(lado1)+float(lado2)+float(lado3)
print("El perimetro del triangulo es: ", perimetro)
#%%
longitud= input("Ingrese la longitud del rectangulo: ")
ancho= input("Ingrese el ancho del rectangulo: ")
area= float(longitud)*float(ancho)
perimetro= 2*(float(longitud)+float(ancho))
print("El area del rectangulo es: ", area)
print("El perimetro del rectangulo es: ", perimetro)
#%%
radio= input("Ingrese el radio del circulo: ")
area= 3.14*float(radio)**2
circunferencia= 2*3.14*float(radio)
print("El area del circulo es: ", area)
print("La circunferencia del circulo es: ", circunferencia)
#%%
x_1= 2
x_2= 6
y_1= 2
y_2= 10
pendiente= input("Ingrese la pendiente de la recta: ")
m= (y_2-y_1)/(x_2-x_1)
print("La pendiente de la recta es: ", m)
distancia= ((x_2-x_1)**2+(y_2-y_1)**2)**0.5
print("La distancia entre los puntos es: ", distancia)
#%%



#%%
len("python") == len("dragón")
palabra1 = "python"
palabra2 = "dragón"
longitud1 = len(palabra1)
longitud2 = len(palabra2)
print(longitud1)
print(longitud2)
#%%
oracion = "Espero que este curso no esté lleno de jerga."
print("jerga" in oracion)
#%%
word1 = "python"
word2 = "dragon"
print("on" in word1 and "on" in word2)
#%%
texto = "python"
longitud = len(texto)
print(longitud)
longitud_float = float(longitud)
print(longitud_float)
longitud_string = str(longitud_float)
print(longitud_string)
#%%
print(7 // 3 == int(2.7))
#%%
dat1= "10"
dat2 = 10
print(dat1 == dat2)
#%%
print(int(9.8) == 10)
#%%
# Solicitar datos al usuario
horas = float(input("Ingresa las horas trabajadas: "))
tarifa = float(input("Ingresa la tarifa por hora: "))
# Calcular el pago total
pago_total = horas * tarifa
# Mostrar resultado
print("El pago total es:", pago_total)
#%%
# Solicitar años al usuario
anios = float(input("Ingresa los años que has vivido: "))
# Convertir años a segundos
segundos = anios * 365 * 24 * 60 * 60
# Mostrar resultado
print("Has vivido aproximadamente", segundos, "segundos")
#%%
print("1", "1", "1", "1", "1")
print("2","1","2","4","8")
print("3","1","3","9","27")
print("4","1","4","16","64")
print("5","1","5","25","125")
