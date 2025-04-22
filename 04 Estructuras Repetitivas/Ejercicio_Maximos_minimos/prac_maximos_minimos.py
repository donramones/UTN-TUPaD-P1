#cant_numeros = 4
#max_num = float ('-inf') #inf para que tenga un maximo como menos infinito por si agregan valores negativos

#for cont in range(cant_numeros):
    #print("Ingrese un numero",(cont+1))
    #num = int (input())
    #if num > max_num:
    #max_num = num
#print("El maximo valor", max_num)

#cant_numeros = 4
#min_num = float ('inf') # inf  si signo arranca de maximo valor

#for cont in range(cant_numeros):
    #print("Ingrese un numero",(cont+1))
    #num = int (input())
    #if num < min_num:
        #min_num = num
#print("El minimo valor", min_num)

#cant_numeros = 4
#max_num = float ('-inf') #inf para que tenga un maximo como menos infinito por si agregan valores negativos
#min_num = float ('inf')

#for cont in range(cant_numeros):
    #print("Ingrese un numero",(cont+1))
    #num = int (input())
    #if num > max_num:
        #max_num = num
    #elif num < min_num:
        #min_num = num
#print("El maximo valor", max_num)
#print("El minimo valor", min_num)


print("Ingrese numero 1")
num = int(input())

cant_numeros = 4
max_num = num
min_num = num
pos_maxima = 1
Pos_minima = 1


for cont in range(2,cant_numeros+1):
    print("Ingrese un numero",cont)
    num = int (input())
    if num > max_num:
        max_num = num
        pos_maxima = cont
    elif num < min_num:
        min_num = num
        Pos_minima = cont
print("El maximo valor", max_num,"y salio en la posicion: ",pos_maxima)
print("El minimo valor", min_num,"y salio en la posicion: ",Pos_minima)

