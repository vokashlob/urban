
# создание класса и методов внутри него
class House:

    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return super().__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не существует!')
        else:
            for i in range(1, new_floor + 1):
                print(i)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __eq__(self, other):
        if isinstance(other, House):
            return len(self) == len(other)

        elif isinstance(other, int):
            return len(self) == other

        else:
            return 'Неверный тип данных'

    def __ne__(self, other):
        if isinstance(other, House):
            return len(self) != len(other)

        elif isinstance(other, int):
            return len(self) != other

        else:
            return 'Неверный тип данных'

    def __lt__(self, other):
        if isinstance(other, House):
            return len(self) < len(other)

        elif isinstance(other, int):
            return len(self) < other

        else:
            return 'Неверный тип данных'

    def __le__(self, other):
        if isinstance(other, House):
            return len(self) <= len(other)

        elif isinstance(other, int):
            return len(self) <= other

        else:
            return 'Неверный тип данных'

    def __gt__(self, other):
        if isinstance(other, House):
            return len(self) > len(other)

        elif isinstance(other, int):
            return len(self) > other

        else:
            return 'Неверный тип данных'

    def __ge__(self, other):
        if isinstance(other, House):
            return len(self) >= len(other)

        elif isinstance(other, int):
            return len(self) >= other

        else:
            return 'Неверный тип данных'

    def __add__(self, other):
        if isinstance(other, House):
            self.number_of_floors = len(self) + len(other)
            return self

        elif isinstance(other, int):
            self.number_of_floors = len(self) + other
            return self

        else:
            return 'Неверный тип данных'

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        return self.__add__(other)

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')


# проверки

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
