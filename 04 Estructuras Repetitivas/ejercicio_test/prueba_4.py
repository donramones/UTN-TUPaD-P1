#ciclo for 2
#desarrollar un algoritmo que permita ingresar una cantidad de personas
#la computadora debe pedir la edad de  cada una y finalmente mostrar el porcentaje de personas 
#que es mayor de edad
edad_minima = 18
cant_personas = int(input("Ingrese una cantidad de personas: "))
cant_personas_mayores = 0

for cont in range (cant_personas):
    print("ingrese la edad n°",(cont+1))
    edad = int(input())
    if edad >= edad_minima:
        cant_personas_mayores += 1
porc = (cant_personas_mayores / cant_personas) * 100
print ("El porcentaje de personas mayores de edad es ",porc)        