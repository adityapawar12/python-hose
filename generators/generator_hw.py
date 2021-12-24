"""
    THIS IS THE HOMEWORK FOR THE GENERATOR SECTION.
"""
import random

# problem no 1
# create a generator that generates squares of numbers.
def gen_sqr(n):
    for i in range(n):
        yield i ** 2

print(list(gen_sqr(10)))

# problem no 2
# create a generator that yields n random numbers between low and high number.
def rand_num(low, high, n):
    for i in range(n): 
        yield random.randint(low, high)

print(list(rand_num(1, 10, 12)))

# problem no 3
# use the iter function to convert string into an iterator.
s = "hello"
s_iter = iter(s)

for i in range(len(s)):
    print(next(s_iter))
