
# исходные данные
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# преобразуем students в сортированный список
# students = sorted(list(students))
students = sorted(students)

# вычисляем среднее для каждой группы оценок
average_grade = [sum(i) / len(i) for i in grades]

# генерируем и выводим на консоль словарь
# grades_dict = {k: v for k, v in zip(students, average_grade)}
grades_dict = dict(zip(students, average_grade))

print(grades_dict)
