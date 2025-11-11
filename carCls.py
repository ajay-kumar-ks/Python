class Engine :
    def __init__(self,power):
        self._power = power
    def display(self):
        print('Power => ',self._power)
        
class Wheels:
    def __init__(self, size):
        self._size = size
    def display(self):
        print('Wheels => ',self._size)
        
class Car(Engine,Wheels):
    def __init__(self, model,power,size):
        Engine.__init__(self,power)
        Wheels.__init__(self,size)
        self._model = model
        
    def display(self):
        Engine.display(self)
        Wheels.display(self)
        print('Model => ',self._model)
        
r1 = Car('r34','1400hp','10 inch')
r1.display()