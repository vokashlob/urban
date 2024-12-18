import threading
from time import sleep
import random


class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!\n')
        enemies = 100
        time_counter = 0
        while enemies > 0:
            time_counter += 1
            enemies -= self.power
            print(f'{self.name} сражается {time_counter} дней(дня), осталось {enemies} воинов.\n')
            sleep(1)

        print(f'{self.name} одержал победу спустя {time_counter} дней(дня)!\n')


first_knight = Knight('Sir Lancelot', random.randrange(10, 60, 10))
second_knight = Knight("Sir Galahad", random.randrange(10, 60, 10))

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')
