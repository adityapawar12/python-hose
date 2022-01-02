"""
    COLLECTIONS MODULE.
"""

from collections import Counter
from collections import defaultdict
from collections import namedtuple

# counter is used to get count of unique items inside a data type.
num_list = [1,2,3,2,2,3,1,2,3,1,34,1,4,1]
char_list = ['a','b','e','d','g','a','b']
char_str = 'my name is aditya'

num_list_c = Counter(num_list)
char_list_c = Counter(char_list)
char_str_c = Counter(char_str)

print(num_list_c)
# most common returns the most appeared item first in a tuple format.
print(char_list_c.most_common())
print(char_str_c)

# default dictionary is just like normal dictionary but it has a defualt value set to it.
d = defaultdict(lambda: 0)

d['first'] = 1
d['second'] = 2
d['nonum']

print(d)
print(d['first'])
print(d['second'])
print(d['nonum'])

# in named tuple we can assign names to the indexes of tuple. it looks more like class.
dog = namedtuple('dog',['name', 'age', 'breed'])
sammy = dog(name='sammy', age=3, breed='husky')

print(sammy.name)
print(sammy[0])
print(sammy.age)
print(sammy[1])
