edad=int(input("Ingrese su edad: "))
if edad > 0 and edad < 12:
    print("eres un niño/a")
elif edad >=12 and edad < 18:
    print("eres un adolecente.")
elif edad >=18 and edad < 30:
    print("Eres un adulto/a joven.")
elif edad >=30:
    print("Eres un adulto/a.")
