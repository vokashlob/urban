import random

numbers = [i for i in range(1, 21)]
given_number = random.randint(3, 20)
answer = []
result = ""

# собираем варианты пар в список

for i in numbers[:given_number]:
    for j in numbers[:given_number]:
        if given_number % (i +j) == 0 and i != j:
            answer.append([i, j])

# удаляем повторы
                
for i in answer:
        for j in answer:
            if i == j[::-1]:
                answer.remove(j)
        
# распаковка вложенных списков

for i in answer:
    for j in i:
        result += str(j) 

result = int(result)


print(f"Число из первой вставки: {given_number}")
print(f"Пароль: {result}")
