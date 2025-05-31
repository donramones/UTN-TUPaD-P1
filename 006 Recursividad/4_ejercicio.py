#Crear una función recursiva en Python que reciba un número entero positivo en base
#decimal y devuelva su representación en binario como una cadena de texto.

def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario (n // 2) + str(n % 2)
numero = 20
print(f"El {numero} en binario es {decimal_a_binario(numero)}")
    