def generate_full_name(firstname, lastname):
    return firstname + ' ' + lastname


def generate_list_from_to(start, to):
    return [i for i in range(start, to+1)]

lambda_x = lambda param1, param2, param3 : param1 if( param1> param2 and param1 > param3) else (param2 if param2 > param3 else param3)

a = lambda_x(1,2,3)

print(a)
