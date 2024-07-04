element: list[int] = [1,2,4,5,6,7]

alphanum: list[int | str] = ["a", 1, 2, 3]

nested: list[list[str]] = [["a", "b"], ["c", "d"]]

# list annotations are not strict
uncaught: list[str] = ["a"]