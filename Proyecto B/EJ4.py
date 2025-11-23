import random

tiradas = 3

def tirardado(tiradas):
    sumatoria = 0
    bandera = True
    while(bandera):
        dado1 = random.randint(1,6)
        dado2 = random.randint(1,6)
        print("Dado 1:", dado1, '\n'
            "Dado 2:", dado2)
        sumatoria = sumatoria + dado1 + dado2
        tiradas = tiradas - 1
        if tiradas == 0:
            bandera = False
    return sumatoria

#sumatoriaFinal = tirardado(tiradas)
#print("Total:", sumatoriaFinal)

jugador1 = tirardado(tiradas)
print("Siguiente jugador")
jugador2 = tirardado(tiradas)

print("Jugador 1:", jugador1, "Jugador 2:", jugador2)