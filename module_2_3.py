
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

number = 0
while True:
    if my_list[number] == 0:
        number += 1
        continue
    elif my_list[number] > 0:
        print(my_list[number])
        number += 1
        continue
    else:
        break
