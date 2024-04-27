import random
import time
from meu_decorador import decorador_mateus

@decorador_mateus
def gerar_numero_aleatorio():
    num = random.randint(1, 10)
    print(num)

if __name__ == "__main__":
    while True:
        gerar_numero_aleatorio()
        time.sleep(1)
