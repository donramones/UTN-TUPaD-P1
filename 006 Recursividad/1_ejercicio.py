#Crea una función recursiva que calcule el factorial de un número.
#Luego, utiliza esafunción para calcular y mostrar en pantalla el factorial de todos los números enteros entre 1 y el número que indique el usuario

def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial (n-1)
    
print(factorial(5))
