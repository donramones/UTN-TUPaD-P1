#Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de masa corporal (IMC)
#Solicitar al usuario los datos y llamar a la fun-ción para mostrar el resultado con dos decimales.

#funciones
def calcular_imc(peso, altura):
    return peso / (altura **2)



#programa principal
 
peso =float(input("ingrse el peso en Kl: "))
altura = float(input("Ingrese la altuira en metros: "))
IMC = calcular_imc(peso, altura)
print(f"El indice de masa corporal es:{IMC}")