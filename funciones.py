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