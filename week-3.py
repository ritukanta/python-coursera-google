#!/usr/bin/env python3

# Loops
# While Loops
# 2
def print_prime_factors(num):
    factor = 2
    while factor <= num:
        if num % factor == 0:
            print(factor)
            num = num/factor
        else:
            factor += 1
    return "Done"


print_prime_factors(100)

# 3


def is_power_of_two(n):
    while n % 2 == 0 and n != 0:
        n = n/2
    if n == 1:
        return True
    return False


print(is_power_of_two(0))
print(is_power_of_two(1))
print(is_power_of_two(8))
print(is_power_of_two(9))


# 4
def sum_divisors(n):
    x = 1
    sum = 0
    while x < n:
        if n % x == 0:
            sum += x
            x += 1
        else:
            x += 1
    return sum


print(sum_divisors(0))
print(sum_divisors(3))
print(sum_divisors(36))
print(sum_divisors(102))

# 5


def multiplication_table(number):
    multiplier = 1
    while multiplier <= 5:
        result = number * multiplier
        if result > 25:
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        multiplier += 1


multiplication_table(3)
multiplication_table(5)
multiplication_table(8)
