'''import dado  # un llamado general'''
import random
from dado import lanzar_dado as lz_dado


def lanzar_dado() -> int:
    return random.randint(10, 20)


for _ in range(10):
    print(lz_dado())
    print(lanzar_dado())
