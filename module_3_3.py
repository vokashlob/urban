
def print_params(a=1, b='FOK JULLE NAAIERS', c=True):
    print(a, b, c)


values_list = ['Kamui', 175, True]
values_list_2 = [777, 'Typical Story']
values_dict = {'a': False, 'b': 'Star Six Seven', 'c': 42}


# print_params(2)
# print_params('鬼卞', 2128506)
# print_params(False, [5, 4, 3, 2, 1], 'WHAT?')
# print_params()
# print_params(b=25)
# print_params(c=[1, 2, 3])
# print_params(*values_list)
# print_params(**values_dict)
print_params(*values_list_2, 42)