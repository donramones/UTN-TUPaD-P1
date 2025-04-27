#Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia
#El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.
total = 0
numero = -1 

while numero != 0:
    try:
        entrada = input("Ingresa un número entero (ingresa 0 para detener): ")
        numero = int(entrada)
        if numero != 0:
            total += numero
    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número entero.")

print(f"El total de los números ingresados es: {total}")



