import threading
import random
from time import sleep


class Bank:

    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            current_deposit = random.randint(50, 500)
            self.balance += current_deposit
            print(f'Пополнение: {current_deposit}. Баланс: {self.balance}')
            sleep(.001)

    def take(self):
        for i in range(100):
            current_take = random.randint(50, 500)
            print(f'Запрос на {current_take}')
            if current_take <= self.balance:
                self.balance -= current_take
                print(f'Снятие: {current_take}. Баланс: {self.balance}')
            else:
                print('Запрос отклонен: недостаточно средств')
                self.lock.acquire()


bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
