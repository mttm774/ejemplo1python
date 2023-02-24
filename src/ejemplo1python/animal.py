
class animal:
    def __init__(self,name):
        self.name=name

    def __str__(self):
        return f'Animal [name={self.name}]'

    def get_name(self):
        return self.name
