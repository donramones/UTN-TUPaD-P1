#ciclo for
#desarrollara un algoritmo que permita ingresar un numero entero entre 1 y 10 (inclusive)
#la computadora debe mostrar la tabla de multiplicacion del numero ingresado

numero = int(input("ingrese un numero entre 1 y 10: "))

if numero >= 1 and numero <= 10:
    for c in range(11):
        print(numero,"x",c,"=",(numero ** c))
else:
    print("No puso un numero entre 1 y 10 ")