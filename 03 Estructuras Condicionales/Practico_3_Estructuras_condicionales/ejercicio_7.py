frase = input("Ingrese una frase o palabra: ")
vocales = "aeiouAEIOU"
if frase and  frase[-1] in vocales:
    resultado = frase + "!"
else:
    resultado = frase