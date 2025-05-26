#Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con el resulta-do de sumarlos,
#estarlos, multiplicarlos y dividirlos. Mostrar los re-sultados de forma clara

#funcion

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    if b != 0:
        divicion = a / b
    else:
        divicion = None
    return (suma, resta, multiplicacion, divicion)

#programa principal

a = float(input("Ingrese el primer numero: "))
b = float(input("Ingrese el segundo numero: "))
suma, resta, multiplicacion, divicion = operaciones_basicas(a, b)
print("resultado suma: ",suma)
print("Resultado resta: ",resta)
print("Resultado multiplicacion: ",multiplicacion)
print("resultado divicion: ",divicion)