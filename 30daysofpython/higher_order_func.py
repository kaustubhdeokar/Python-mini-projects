# to pass functions as arguments

def sum_of_nums(nums):
    return sum(nums)

def cubes_of_nums(nums):
    return [i*i*i for i in nums]

def higher_order_functions(func, list1):
    func_exec = func(list1)
    return func_exec

output = higher_order_functions(cubes_of_nums, [1,2,3])

print(output)
