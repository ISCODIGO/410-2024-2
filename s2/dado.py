# Funcion para simular un lanzamiento de dados
import random


def lanzar_dado() -> int:
    return random.randint(1, 6)


for _ in range(10):
    print(lanzar_dado())
