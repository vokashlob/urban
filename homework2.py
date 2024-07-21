homeworks_count = 12
hours_spent = 1.5
course_name = 'Python'
average_time = hours_spent / homeworks_count

print('Курс:', course_name, ', всего задач:', homeworks_count, ', затрачено часов:', hours_spent, ', среднее время выполнения:', average_time, 'часа или', average_time * 60, 'минут.')

# Поскольку Python сам ставит пробелы после переменных, перечисленных в скобках функции print,
# то, с точки зрения пунктуации, лучше отформатировать вывод через f-strings:

print(f'Курс: {course_name}, всего задач: {homeworks_count}, затрачено часов: {hours_spent}, среднее время выполнения: {average_time} часа или {average_time * 60} минут.')
