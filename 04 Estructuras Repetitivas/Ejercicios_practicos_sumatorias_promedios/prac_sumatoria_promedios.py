
#sumatoria de numeros y mostrarlos por panatalla

cant_numeros = 5
sumatoria = 0
for cont in range (1,cant_numeros+1):
    print("ingrese numero",cont)
    num = int(input())
    sumatoria = sumatoria + num #sumatoria += num ; cont += 1
print("La sumatoria de los valores es: ",sumatoria)
#agrego una linea para calcular el promedio,ya cuento con las veriables sumatoria/cant_numeros
print("El promedio es: ",(sumatoria/cant_numeros))