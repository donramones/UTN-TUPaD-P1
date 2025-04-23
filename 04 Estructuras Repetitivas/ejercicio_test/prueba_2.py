#control de ciclos por bandera
#desarrollar un algoritmo  que permita ingresar el nombre y la edad(por separado)
#de diferentes personas, la carga termina cuando en el nombre de la proxima persona se ingresa
#un asterisco, la pc debe mostrar como se llama la persona mas jove.

CORTE = "*"
Nombre_incorrecto = "zzzzzzzzzzz"
edad_minima = float("inf")
nombre_mas_joven = Nombre_incorrecto
nombre = input("Ingrese su nombre (" + CORTE + " para cortar): ")
while nombre != CORTE:
    edad = int(input("Ingrese la edad de: " + nombre + ": "))
    if edad < edad_minima:
        edad_minima = edad
        nombre_mas_joven = nombre
    nombre = input("Ingrese otro nombre (" + CORTE + " para cortar): ")
if nombre_mas_joven == Nombre_incorrecto:
    print("no ingresaron personas")
else:
    print("La persona mas joven (",edad_minima," años)es",nombre_mas_joven)