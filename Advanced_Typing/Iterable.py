from typing import Iterable, Literal

def list_elements(elements: Iterable) -> None:
    for i, element in enumerate(elements, start=1):
        print(i, element, sep=': ')
        
    
people: Literal[str] = ('Damilola', 'Luigi', "Farouq")

list_elements(people)