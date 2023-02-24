import sys

from src.ejemplo1python.animal import animal
from src.ejemplo1python.mammal import mammal


if __name__ == "__main__":

    print("como se llama el animal")
    nombre=input()
    filled=True
    y=2.8
    p=34/5
    print (p)

    mi_animal=animal(nombre)
    print(mi_animal)
    print('hola')

    mi_mammal=mammal('delfin')
    print(mi_mammal)
    