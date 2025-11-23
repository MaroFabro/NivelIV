import random

bandera = True
tiradas = 2
sumatoria = 0

while(bandera):
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)
    print("Dado 1:", dado1, '\n'
          "Dado 2:", dado2)
    sumatoria = sumatoria + dado1 + dado2
    tiradas = tiradas - 1
    if tiradas == 0:
        bandera = False
    
print("Total:", sumatoria)    
