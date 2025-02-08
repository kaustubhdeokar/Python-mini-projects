
## decorators - class and function decorators.

# this will add new functionality to the underlying function, kinda extending the functionality of it.
# without modifying it.
# functions in python are first class objects - they can be passed to a function, returned from a function.
def print_info(func):
    school = 'S1'
    city = 'c1'
    def wrapper(*args, **kwargs):
        print(f'School is {school}')
        func(*args, **kwargs)
        print(f'City is {city}')
    return wrapper

#@print_info if this is not present
def print_name():
    print('Alex')

#if the decorator is not present above print_name method, then we can pass function to the print_info
# where we can get the enhancement in the function print_info + our function executed.
p = print_info(print_name)
p()

## instead of this, we can just do

@print_info
def print_name_2():
    print('Name2')
print(print_name_2())

# if the method takes any argument, this will throw out an error,
# because the function when called inside the decorator function should contain the same arguments,
# hence we use *args, **kwargs

@print_info
def print_name_3(name):
    print(name)

def repeat(func):
    def wrapper(*args, **kwargs):
        print('do something')
        func(*args, **kwargs)
        print('do something else')

def repeat2(num_times):
    def decorator_func(func):
        def wrapper(*args, **kwargs):
            print('do something')
            for _ in range(num_times):
                r = func(*args, **kwargs)
            print('do something else')
            return r
        return wrapper
    return decorator_func

@repeat2(num_times=4)
def count_to_10():
    for i in range(1,11):
        print(i, end=' ')
    return 'ok'

print(count_to_10())

## we can apply multiple decorators , they will execute as we have defined them top to botom

class Count:
    def __init__(self, func):
        self.num_calls = 0
        self.func = func
        self.cache = {}

    def __call__(self, *args, **kwargs):
        self.num_calls +=1
        print(f"args:{args}")
        if args not in self.cache:
            print(f"num of calls {self.num_calls}")
            self.cache[args] = self.func(*args, **kwargs)
            return self.cache[args]
        return self.cache[args]


@Count
def fibonacci(n):
    if n==0 or n==1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))