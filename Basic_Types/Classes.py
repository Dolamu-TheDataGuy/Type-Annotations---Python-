class Fruit:
    def __init__(self, name: str, grams: float):
        self.name = name
        self.grams = grams
        
orange: Fruit = Fruit(name='Orange', grams=100)

def describe(fruit: Fruit):
    print(f'{fruit.name} weighs {fruit.grams} grams')
    
Apple = 'Apple'
    
describe(orange)
describe(Apple)

