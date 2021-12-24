"""
    PYTHON GENERATORS PRACTICE.
"""

# normal function
def create_cubes(n):

    result = []

    for i in range(n):
        result.append(i ** 3)

    return result


print(create_cubes(10))

# generator function 
def create_cubes_g(n):

    for i in range(n):
        yield i ** 3

print(list(create_cubes_g(10)))
