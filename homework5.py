immutable_var = 42, 36.6, 'Guido van Rossum', True

print(immutable_var)

# immutable_var[1] = 37.7 # приводит к TypeError - объект "кортеж" не поддерживает присвоение значений элементам (т.е. является неизменяемым)

mutable_list = [len(immutable_var), 'lists are mutable type', 45 in immutable_var]

print(mutable_list)

mutable_list[0] = mutable_list[0] ** 0.5
mutable_list[1] = mutable_list[1].upper()
mutable_list[2] = 45 not in immutable_var

print(mutable_list)
