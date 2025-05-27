#Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en Fahrenheit.
#Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.

#funcion
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32


#programa principal
celsius = float(input("Ingrese la temperatura en grados celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)
print(f"La temperatura ingresada en celsius: {celsius} corresponde a {fahrenheit} fahrenheit")