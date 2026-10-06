def func1(param1, param2):
    print(param1)
    print(param2)
    print(param1 + param2)

def unpack_multiple(*nums):
    total = 0
    for num in nums:
        total += num
    return total


def generate_groups (team,*args):
    print(team)
    for i in args:
        print(i)


def greet(name, location):
    print("Hi there", name, "how is the weather in", location)

greet(name="Alice", location="New York")  


my_dict = {"name": "Alice", "location": "New York"}

greet(**my_dict)
