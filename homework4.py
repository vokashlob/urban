my_string = input('Введите произвольный текст: ')
length = len(my_string)
ending_digits_var0 = (2, 3, 4)
ending_digits_var1 = (0, 5, 6, 7, 8, 9)

# if length % 10 in ending_digits_var0:
#     ending = 'а'
# elif length % 10 in ending_digits_var1:
#     ending = 'ов'
# else:
#     ending = ''

ending = 'a' if length % 10 in ending_digits_var0 else ('ов' if length % 10 in ending_digits_var1 else "")

print('Во введенной Вами строке', length, 'символ' + ending)
print('Заглавные:', my_string.upper())
print('Прописные:', my_string.lower())
print('Без пробелов:', my_string.replace(' ', ''))
print('Первый символ строки:', my_string[0])
print('Последний символ строки', my_string[-1])
