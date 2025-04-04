EDAD_MINIMA = 21

edad= int(input("Ingrese su edad: "))
categoria= input("Ingrese su categoria (A, B, C, D, E, F, G): ")

#se agrega () a (categoria == "D" or categoria == "d"): , para evaluar dos resultados
if edad >= EDAD_MINIMA and (categoria == "D" or categoria == "d"):
    print("Puede conducir ambulancias")
else:
    print("No puede conducir ambulancias")