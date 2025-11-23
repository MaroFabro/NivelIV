vidas = int(input("ingrese un número de vidas:"))
if vidas >= 5:
    print("Dificultad: FÁCIL")
else:
    if vidas == 3 or vidas == 4:
        print("Dificultad: MEDIO")
    else:
        print("Dificultad: DIFÍCIL")