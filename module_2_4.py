
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in numbers[1:]:
    temp_list = numbers[1:numbers.index(i)]
    is_prime = True
    for j in temp_list:
        if i % j == 0:
            is_prime = False
    if is_prime == True:
        primes.append(i)
    else:
        not_primes.append(i)

print(primes)
print(not_primes)







