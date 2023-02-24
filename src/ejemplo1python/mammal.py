from src.ejemplo1python.animal import animal


class mammal(animal):
    def __init__(self,name):
        self.name=name

    def __str__(self):
         return f'Mammal [name={self.name}]'