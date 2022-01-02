"""
    MATH AND RANDOM MODULES.
"""

import math
import random

# for getting help about the math module.
# help(math)

value1 = 2.5
value2 = 3.5

# some of useful math functions
print(math.floor(value1), math.ceil(value2))
round(2.5)
round(3.5)
print(math.pi, math.e, math.inf, math.nan)
print(math.sin(math.pi/2))
print(math.degrees(math.pi), math.radians(180))
print(math.log(100, 10))

# some of random module functions.
print(random.randint(0, 100))
ran_list = list(range(30))

print(random.choice(ran_list))
print(random.choices(population=ran_list, k=10))
print(random.sample(population=ran_list, k=10))
print(ran_list)
random.shuffle(ran_list)
print(ran_list)
print(random.uniform(a=0, b=100))
print(random.gauss(mu=0, sigma=1))

# random.seed(101)
# print(random.randint(0, 100))
# print(random.randint(0, 100))
