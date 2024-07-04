# x = 1

# x = "tim"

# Type hint

# x: int = 1
# print(x + 1)

# def add_num(a: int, b: int, c: int) -> int:
#     return a + b + c

# print(add_num(1,3,5))

from typing import List, Dict, Set, Optional, Any, Sequence, Tuple, Callable

# x: List[List[int]] = [[1, 2], [3, 4]]

# x: dict[str, str] = {"a": "b"}

# x: Set[str] = {"a", "b"}

## Custom types

# Vector = List[float]

# def foo(v: Vector) -> Vector:
#     print(v)

# foo()

# Vector = List[float]

# Vectors = List[Vector]

# def foo(v: Vectors) -> Vector:
#     pass

# foo()

## Optional Types

# def foo(output: Optional[bool]=False):
#     pass

# foo() 

## Any Type

# def foo(output: any):
#     pass


## Sequence

# def foo(seq: Sequence[str]):
#     pass

# foo(("a", "b", "c"))
# foo(["a", "b", "c"])
# foo("hi")
# foo({1, 2, 3})

## Tuple type

# x: Tuple[int, int, int, str]= (1,2,3,'Hello')

# def foo(seq: Sequence[str]):
#     pass

## Callable Types

def add(x: int, y:int) -> int:
    return x+y

# def foo() -> Callable[[int, int], int]:
#     def add(x: int, y:int) -> int:
#         return x+y
    
#     return add

# foo(add)

