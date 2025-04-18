#ciclo infinito
#print("Hola")
#while 2==3:
    #print("repetir_ciclo")
#print("Chau")
#///////////////////////////////////////////////////////////
#centinela
umbral = 10
sumatoria = 0
cont = 0
while sumatoria < umbral:
    cont += 1 #cont = cont + 1
    print("ingrese un numero")
    num = int(input())
    sumatoria += num #sumatoria = sumatoria + num
    

print("El promedio de valores es: ",(sumatoria/cont))