#Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado.
#Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de-volver: “Hola Marcos!”
#Llamar a esta función desde el programa principal solicitando el nombre al usuario

#funcion

def saludar_usuario(nombre):
    return f"Hola {nombre}!"



#programa principal
nombre = input("Ingrese su nombre: ")
saludo= saludar_usuario(nombre)
print(saludo)

