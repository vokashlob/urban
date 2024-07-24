
# словари

keys = [i for i in range(1, 11)]
values = [i ** 2 for i in range(1, 11)]
my_dict = {k: v for k, v in zip(keys, values)}
print('Словари:', '\n')
print('Dictionary:', my_dict)
print('Existing value:', my_dict[5])
print('Non-existent value:', my_dict.get(11))

my_dict.update({11: 11 ** 2, 12: 12 ** 2})

print('Deleted value:', my_dict.pop(10))
print('Modified dictionary:', my_dict)
print('\n')

# множества

my_list = (keys + values) * 2
my_set = set((keys + values) * 2)

# print(my_list, my_set) # показательная работа команды set(), удаляющая повторяющиеся значения
print('Множества:', '\n')
print('Set', my_set)
my_set.update({1973, 2024})
my_set.discard(100)
print('Modified set', my_set)
