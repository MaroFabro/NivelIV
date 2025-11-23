for i in range (5):
    vidas = int(input("ingrese vidas"))
    if vidas >= 5:
        print("Dificultad: FÁCIL")
    else:
        if vidas == 3 or vidas == 4:
            print("Dificultad: MEDIO")
        else:
            print("Dificultad: DIFÍCIL")