import time
import timeit

def func_one(n):
    return [str(num) for num in range(n)]

def func_two(n):
    return list(map(str,range(n)))

start_time = time.time()
func_one(1000000)
end_time = time.time()
elasped_time = end_time - start_time
print(elasped_time)

start_time = time.time()
func_two(1000000)
end_time = time.time()
elasped_time = end_time - start_time
print(elasped_time)

stmt1 = '''
func_one(100)
'''

stmt2 = '''
func_two(100)
'''

setup1 = '''
def func_one(n):
    return [str(num) for num in range(n)]
'''

setup2 = '''
def func_two(n):
    return list(map(str,range(n)))
'''

print(timeit.timeit(stmt1, setup1, number=100000))
print(timeit.timeit(stmt2, setup2, number=100000))
