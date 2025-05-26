#Crear dos funciones: calcular_area_circulo(radio) que reciba el ra-dio como parámetro y devuelva el área del círculo.
#calcular_peri-metro_circulo(radio) que reciba el radio como parámetro y devuel-va el perímetro del círculo
#Solicitar el radio al usuario y llamar am-bas funciones para mostrar los resultados.

#funciones

pi = 3.14
def calcular_area_circulo(radio):
    return pi * radio ** 2
    

def calcular_peri_metro_circulo(radio):
    return 2 * pi * radio



#Programa principal
radio = float(input("Ingrese el radio del circulo: "))
area = calcular_area_circulo (radio)
perimetro = calcular_peri_metro_circulo (radio)

print(f"el area del circulo es: {area}, el perimetro es {perimetro}")


