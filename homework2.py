homeworks_count = 12
hours_spent = 1.5
course_name = 'Python'
average_time = hours_spent / homeworks_count

print('Курс: ' + course_name + ', всего задач: ' + str(homeworks_count) + ', затрачено часов: ' + str(hours_spent) + ', среднее время выполнения: ' + str(average_time) + ' часов или ' + str(average_time * 60) + ' минут.')

# менее громоздкий вариант, не требующий, к тому же, приведения типов
print(f'Курс: {course_name}, всего задач: {homeworks_count}, затрачено часов: {hours_spent}, среднее время выполнения: {average_time} часов или {average_time * 60} минут.')