
def calcular_suma (numero_limite):
if numero_limite <= 0:
    return "Por favor, ingresa un número entero positivo."
  else:
    suma = 0
    for numero in range(numero_limite + 1):
      suma += numero
    return suma
try:
  limite = int(input("Ingresa un número entero positivo: "))
  resultado = calcular_suma(limite)
  print(f"La suma de los números desde 0 hasta {limite} es: {resultado}")
except ValueError:
  print("Entrada inválida. Por favor, ingresa un número entero.")