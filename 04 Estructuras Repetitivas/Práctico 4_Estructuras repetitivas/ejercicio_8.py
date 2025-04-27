#Escribe un programa que permita al usuario ingresar 100 números enteros
#Luego, elprograma debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos.
#(Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio)

#1-variables:
par=0
impar=0
negativo=0
positivo=0

for cont in range (10):
    numero_ingresado=int(input("Ingrese un numero: "))
    if numero_ingresado >0:
        positivo += 1
    if numero_ingresado %2==0:
        par += 1
    if numero_ingresado <0:
        negativo += 1
    if numero_ingresado %2 !=0:
        impar += 1
    
print(  "Los numeros ingresados corresponde a : "   )
print("Numero par: ",par)
print("Numero impar: ",impar)
print("Numero negativo: ",negativo)
print("Numero positivo: ",positivo)