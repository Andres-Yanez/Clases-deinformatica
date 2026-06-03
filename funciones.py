def generate_full_name():
    first_name = "Andres"
    last_name = "Yanez"
    space = " "
    full_name= first_name + space + last_name
    print(full_name)
generate_full_name()
print("------")
generate_full_name()

def mostrar_instrucciones():
    print("===INSTRUCCIONES DE PROGRAMA ===")
    print("1. Ingresa tu nombre.")
    print("2. Ingresa tu edad.")
    print("3. El programa mostrara un mensaje personalizado.")
def mostrar_despedida():
    print("Gracias por usar el programa")
print("===SISTEMA DE REGISTRO===")
opcion = input("¿Deseas ver las instrucciones? si/no: ")
if opcion =="si":
    mostrar_instrucciones()
nombre = input("Ingrese su nombre: ")
edad= input("Ingrese su edad: ")
print(f"Hola {nombre}, tienes {edad} años")
mostrar_despedida()      


def mostrar_instrucciones():
    print('=== INSTRUCCIONES ===')
    print('Debe ingresar dos números.')
    print('El programa sumará esos números.')
    print('Puede escribir ayuda si no entiende qué hacer.')
print('=== SUMA DE DOS NÚMEROS ===')
mostrar_instrucciones()
dato = input('Ingrese el primer número o escriba ayuda: ')
if dato == 'ayuda':
    mostrar_instrucciones()
    dato = input('Ingrese el primer número: ')
numero1 = int(dato)
numero2 = int(input('Ingrese el segundo número: '))
suma = numero1 + numero2
print(f'La suma es: {suma}')

def saludar(nombre):
    print(f"Hola {nombre}")
saludar("Andres")

#%%
def mostrar_estudiante(nombre, curso):
    print("== DATOS DEL ESTUDIANTE ==")
    print(f"Nombre: {nombre}")
    print(f"Curso: {curso}")
    print("--------------------------")
def mensaje_final():
    print("Fin del programa")
cantidad = int(input("¿Cuántos estudiantes desea ingresar?: "))
contador = 0
while contador < cantidad:
    nombre = input("Ingrese el nombre del estudiante: ")
    curso = input("Ingrese el curso del estudiante: ")
    mostrar_estudiante(nombre, curso)  
    contador += 1  
mensaje_final()
#%%
def calcular_promedio(nota1, nota2, nota3, nombre, apellido):
    promedio = (nota1 + nota2 + nota3) / 3
    print("---RESULTADO---")
    print("Nombre completo:", nombre, apellido)
    print("Notas:", nota1, nota2, nota3)
    print("Promedio:", promedio)
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))
calcular_promedio(nota1, nota2, nota3, nombre, apellido)
#%%
def obtener_mensaje():
    mensaje = "Bienvenido al sistema"
    return mensaje
def generar_nombre_completo():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    nombre_completo = f"{nombre} {apellido}"
    return nombre_completo
print(obtener_mensaje())
print(generar_nombre_completo())

# Función
def calcular_total_producto(precio, cantidad):
    return precio * cantidad


# Programa principal
print("=== SISTEMA DE COMPRA ===")

subtotal = 0

for i in range(1, 4):
    print(f"\nProducto {i}")
    
    nombre = input("Ingrese el nombre del producto: ")

    # Validar precio
    precio = float(input("Ingrese el precio del producto: "))
    while precio <= 0:
        print("Precio no válido. Debe ser mayor que 0.")
        precio = float(input("Ingrese nuevamente el precio del producto: "))

    # Validar cantidad
    cantidad = int(input("Ingrese la cantidad comprada: "))
    while cantidad <= 0:
        print("Cantidad no válida. Debe ser mayor que 0.")
        cantidad = int(input("Ingrese nuevamente la cantidad comprada: "))

    # Calcular total del producto
    total_producto = calcular_total_producto(precio, cantidad)

    # Acumular
    subtotal += total_producto

    print(f"Producto registrado: {nombre}")
    print(f"Total del producto: ${total_producto:.2f}")


# Cálculos finales
iva = subtotal * 0.15
total_pagar = subtotal + iva

# Resultados
print("\n=== RESUMEN DE COMPRA ===")
print(f"Subtotal: ${subtotal:.2f}")
print(f"IVA (15%): ${iva:.2f}")

#Ejercicios
#%%
def metros_a_centimetros(metros):
    return metros * 100
def metros_a_milimetros(metros):
    return metros * 1000
def metros_a_kilometros(metros):
    return metros / 1000
def metros_a_pulgadas(metros):
    return metros * 39.3701
def main():
    print("=== Conversor de unidades ===")
    metros = float(input("Ingrese la cantidad en metros: "))
    while True:
        print("\nSeleccione una opción:")
        print("1. Convertir a centímetros")
        print("2. Convertir a milímetros")
        print("3. Convertir a kilómetros")
        print("4. Convertir a pulgadas")
        print("5. Salir")
        opcion = input("Ingrese su opción: ")
        if opcion == "1":
            resultado = metros_a_centimetros(metros)
            print(f"{metros} metros = {resultado} cm")
        elif opcion == "2":
            resultado = metros_a_milimetros(metros)
            print(f"{metros} metros = {resultado} mm")
        elif opcion == "3":
            resultado = metros_a_kilometros(metros)
            print(f"{metros} metros = {resultado} km")
        elif opcion == "4":
            resultado = metros_a_pulgadas(metros)
            print(f"{metros} metros = {resultado} pulgadas")
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, intente nuevamente.")
if __name__ == "__main__":
    main()

# %%
def calcular_promedio(n1, n2, n3):
    return (n1 + n2 + n3) / 3
def nota_mayor(n1, n2, n3):
    return max(n1, n2, n3)
def nota_menor(n1, n2, n3):
    return min(n1, n2, n3)
def estado_estudiante(promedio):
    if promedio >= 70:
       print(f"Aprueba")
    else:
        print(f"Reprueba")
n1 = float(input("Ingrese la primera nota: "))
n2 = float(input("Ingrese la segunda nota: "))
n3 = float(input("Ingrese la tercera nota: "))
while True:
    print("\nMENÚ")
    print("1. Calcular promedio")
    print("2. Mostrar nota mayor")
    print("3. Mostrar nota menor")
    print("4. Determinar si aprueba o reprueba")
    print("5. Salir")
    opcion = input("Escoja una opción: ")
    if opcion == "1":
        print(f"Promedio: {calcular_promedio(n1, n2, n3)}")
    elif opcion == "2":
        print(f"Nota mayor: {nota_mayor(n1, n2, n3)}")
    elif opcion == "3":
        print(f"Nota menor: {nota_menor(n1, n2, n3)}")
    elif opcion == "4":
        prom = calcular_promedio(n1, n2, n3)
        print(f"Estado: {estado_estudiante(prom)}")
    elif opcion == "5":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida, intentelo de nuevo ")

# %%
