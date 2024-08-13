
first = int(input("Введите первое число:  \n"))
second = int(input("А теперь второе число: \n"))
third = int(input("И, наконец, третье: \n"))

if first == second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)