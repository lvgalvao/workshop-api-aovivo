import random
import time

def numero_aleatorio():
    return random.randint(1,10)

def dobra_um_nomero(num):
    return num * 2

if __name__ == "__main__":
    while True:
        num = numero_aleatorio()
        resultado = dobra_um_nomero(num)
        print(f"O dobro de {num} é {resultado}")
        time.sleep(1)
