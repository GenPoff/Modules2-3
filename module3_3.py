def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()
print_params('String', 5, 1908)
print_params(b = 25)
print_params(c = [1,2,3])

values_list = ['Boba', True, 3]
values_dict = {'a': 'Biba', 'b': 9.46, 'c': False}


values_list_2 = [7, 'Seven']

print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)
