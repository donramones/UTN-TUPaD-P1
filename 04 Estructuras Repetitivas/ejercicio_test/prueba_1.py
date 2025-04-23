#desarrollar programa que permita ingresar un numero entero positivo. La computadora debe mostrar  la sucesion  de numeros  desde el numero ingresado hasta el cero
#en una sola linea
#numero = int(input("Ingrese un numero positivo: "))

#if numero >0:
    #cont = numero
    #while cont >= 0:
        #print(cont)
        #cont = cont -2

#else:
    #print("El numero deberia ser positivo")

numero = int(input("Ingrese un numero positivo: "))

if numero >0: 
    if  numero % 2 != 0: #para verificar numeros impares , utilizo % que me devuelve el resto si es diferente a cero le resto uno
        numero = numero -1 # se le resta uno por si ingresa un numero impar
    cont = numero
    while cont >= 0:
        print(str(cont) + " ", end="") #ens="" salto de linea , str funcion que permite convertir a cadena cualquier numero
        cont = cont -2

else:
    print("El numero deberia ser positivo")