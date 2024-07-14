from typing import Any
from sys import getsizeof


def display_size(user_input: Any) -> None:
    print(f'{user_input} -> {getsizeof(user_input)} bytes')
    

display_size([1,2,3])
display_size(9)
display_size("Welcome to Pycon Nigeria")
display_size(None)