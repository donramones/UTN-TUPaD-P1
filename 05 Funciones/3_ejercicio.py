#Crear una función llamada informacion_personal(nombre, apellido,edad, residencia)
#que reciba cuatro parámetros e imprima: “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”
#Pe-dir los datos al usuario y llamar a esta función con los valores in-gresados.

#funcion
def informacion_personal(nombre, apellido,edad, residencia):
    return f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}"



#Programa principal
nombre = input("Ingrese  su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese lugar de residencia: ")
valores_ingresados = informacion_personal (nombre, apellido,edad, residencia)
print(valores_ingresados)




