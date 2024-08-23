
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


# проверки

h1 = House('Эдьбрус', 25)
h2 = House('Машук', 2)
h3 = House('Казбек', 0)
h1.go_to(5)
h2.go_to(10)
h3.go_to(10)
