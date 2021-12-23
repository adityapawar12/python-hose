"""
    THE DECORATOR PRACTISE.
"""

# assigning value of function to a variable.
def hello():
    return "hello"

hello_var = hello

print(hello)
del hello
print(hello_var())

# function inside of another function.
def func_one():
    print("this is the function no 1.")

    def func_two():
        return("\t this is the function no 2.")

    print(func_two())

func_one()

# function returning another function.
def fun_one():
    return "this is function one"
    
def fun_two(fun):
    print("this is function two")
    print(fun())

fun_two(fun_one)

# decorator function.
def new_decorator(original_fun):

    def wrap_func():

        print("some extra code before the original function.")

        original_fun()

        print("some extra code after the original function.")

    return wrap_func

def func_needs_decorator():
    print("i want to be decorated.")

# manually decorating a function
decorated_func = new_decorator(func_needs_decorator)
decorated_func()

# using @ for decorator function
@new_decorator
def func_needs_decorator():
    print("i want to be decorated.")

func_needs_decorator()
