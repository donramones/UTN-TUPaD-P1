#Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad de horas correspondientes
# Solicitar al usuario los segundos y mos-trar el resultado usando esta función.

#funciones
def segundos_a_horas(segundos):
    return segundos / 3600




#programa principal

segundos =float(input("Ingrese los segundos: "))
horas = segundos_a_horas(segundos)
print(f"los {segundos} segundos ingresados corresponde a {horas} horas")

