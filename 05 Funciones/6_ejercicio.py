#Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese número del 1 al 10
#Pedir al usuario el número y llamar a la fun-ción.

#funcion

def tabla_multiplicar(numero):
    print(f"tabla de multiplicar {numero}: ")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
    


#programa principal

numero = int(input("ingrese un numero: "))
tabla_multiplicar(numero)

