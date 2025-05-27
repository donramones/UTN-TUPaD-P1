#Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos
#Solicitar los números al usuario y mostrar el resultado usando esta función

#funcion
def calcular_promedio(a, b, c):
    return (a + b + c) /3





#programa principal
a = float(input("Ingrese primer numero: "))
b = float(input("Ingrese segundo numero: "))
c = float(input("Ingrese tercero numero: "))
promedio = calcular_promedio(a, b, c)
print(f"el promedio de los numero {a}, {b}, {c} es: {promedio}")

