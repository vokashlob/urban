
def is_prime(func):
    def wrapper(*args):
        number = func(*args)
        if number <= 0:
            print("Не простое")
            return number
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                print("Составное")
                return number
        print("Простое")
        return number
    return wrapper

@is_prime
def sum_three(a, b, c):
    result = a + b + c
    return result


result = sum_three(2, 3, 6)
print(result)
