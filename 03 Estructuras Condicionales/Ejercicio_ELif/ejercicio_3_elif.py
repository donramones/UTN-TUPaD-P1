edad = int(input("Introduce tu edad: "))

if edad >= 0 and edad <=12:
    print("eres un niño")
elif edad >=13 and edad <= 17:
    print("eres un adolecente.")
elif edad >=18 and edad <= 64:
    print("Eres un adulto.")
else:
    print("Eres un adulto mayor.")
    