#Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacios ni tildes
#y devuelva True si es un palíndromo o False si no lo es

def es_polindromo (texto):
    if len(texto) <=1:
        return True
    if texto[0] != texto [-1]:
        return False
    return es_polindromo (texto[1:-1])

print(es_polindromo("ada"))
