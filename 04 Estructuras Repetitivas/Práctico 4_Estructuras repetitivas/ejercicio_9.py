#Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores.

valor_final = 10
suma = 0

for con in range(valor_final):
    num_1= float(input("ingrese un numero: "))
    suma += num_1
media = suma/valor_final

print("La media de los numero ingresados es: ",media)