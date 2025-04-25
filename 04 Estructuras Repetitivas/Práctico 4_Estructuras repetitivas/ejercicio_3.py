
num_min =input("Introduce el primer número entero: ")
num_maximo =input("Introduce el segundo número entero: ")

valor1 = int(num_min)
valor2 = int(num_maximo)
 # Calcular la suma de los enteros entre los valores
resultado_suma = (valor1 + valor2)

  # Mostrar el resultado
if resultado_suma :
    print(f"La suma de los enteros entre {valor1} y {valor2} (excluidos) es: {resultado_suma}")
else:
    print("Error: Uno o ambos valores introducidos no son números enteros válidos.")