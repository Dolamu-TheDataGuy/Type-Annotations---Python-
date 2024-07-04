from typing import Optional

person: Optional[str] = None

def greet(name: str | None = None):
    if name is None:
        print('No one is here...')
    else:
        print(f'Hello, {name}')
        
greet()