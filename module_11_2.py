# библиотеки
import pprint
import inspect


# функция
def introspection_info(obj):
    info_dict = {'Тип данных': type(obj)}
    try:
        info_dict['Имя объекта'] = obj.__name__
    except AttributeError:
        info_dict['Имя объекта'] = 'у этого объекта нет атрибута __name__'

    # обработка dir()
    attr_list = []
    for i in dir(obj):
        if not i.startswith('__') and not i.endswith('__'):
            attr_list.append(i)
    if len(attr_list):
        attr_description = []
        for attr_name in attr_list:
            attr = getattr(obj, attr_name)
            attr_description.append([attr_name, type(attr)])
        info_dict["Функции, методы и атрибуты (кроме dunder'ов)"] = attr_description
    else:
        info_dict["Функции, методы и атрибуты (кроме dunder'ов)"] = 'нет'

    if inspect.getmodule(obj):
        info_dict['Принадлежность к модулю'] = inspect.getmodule(obj)
    else:
        info_dict['Принадлежность к модулю'] = 'нет'

    if callable(obj):
        info_dict['Может быть вызван'] = 'да'
    else:
        info_dict['Может быть вызван'] = 'нет'


    pprint.pprint(info_dict)
    print('\n')


# строка
txt = 'В лесу родилась ёлочка'

# число
number = 13

# список
lst = [[i ** i] for i in range(1, 10)]

# словарь
d = {x: y for x, y in zip(range(1, 10), lst)}


# класс
class MyClass:
    def __init__(self):
        self.name = 'MyClassName'
        self.attribute = 42

    def method(self, num):
        if isinstance(num, int) or isinstance(num, float):
            self.attribute += num
            print(self.attribute)
        else:
            print('Error')

    def __private_method(self):
        pass


# экземпляр класса
obj_1 = MyClass()

# анализ объектов
objects = [pprint, introspection_info, txt, number, lst, d, MyClass, obj_1]
for obj in objects:
    introspection_info(obj)
