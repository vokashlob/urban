
def custom_write(filename, strings):
    file = open(filename, 'w', encoding='utf-8')
    counter = 0
    string_positions = {}
    for string in strings:
        cursor = file.tell()
        file.write(string + '\n')
        counter += 1
        string_positions[(counter, cursor)] = string
    file.close()
    return string_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)