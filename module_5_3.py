
# создание класса и методов внутри него
class House:
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
            return len(self) + len(other)

        elif isinstance(other, int):
            return len(self) + other

        else:
            return 'Неверный тип данных'

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        return self.__add__(other)



# проверки

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__

h1 = h1 + 2.5
print(h1)

