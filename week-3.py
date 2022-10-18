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


# for loops
# 2
def factorial(n):
    result = 1
    for x in range(1, n):
        result *= x
    return result


for n in range(0, 10):
    print(n, factorial(n + 1))

# 3
for y in range(1, 11):
    print(y**3)


# 4
for m in range(101):
    if m % 7 == 0:
        print(m)

# 5


def retry(operation, attempts):
    for t in range(attempts):
        if operation():
            print("Attempt " + str(t) + " succeeded")
            break
        else:
            print("Attempt " + str(t) + " failed")


#retry(create_user, 3)
#retry(stop_service, 5)


# Recursion
# 3
def is_power_of(number1, base):
    if number1 < base:
        return number1 == 1
    return is_power_of(number1//base, base)


print(is_power_of(8, 2))
print(is_power_of(64, 4))
print(is_power_of(70, 10))


# 4
# def count_users(group):
# count = 0
# for member in get_members(group):
#  if is_group(member):
#     count += count_users(member)
#  else:
#     count += 1
# return count


# print(count_users("sales"))
# print(count_users("engineering"))
# print(count_users("everyone"))

# 5


def sum_positive_numbers(k):
    if k == 0:
        return 0
    return k + sum_positive_numbers(k-1)


print(sum_positive_numbers(3))
print(sum_positive_numbers(5))


# Module 3 Graded Assessment
# 1
numb = 1
while numb <= 7:
    print(numb, end=" ")
    numb += 1

# 2


def show_letters(word):
    for w in word:
        print(w)


show_letters("Hello")

# 3


def digits(i):
    count = 0
    if i == 0:
        return 1
    while i >= 1:
        count += 1
        i = i/10
    return count


print(digits(25))
print(digits(144))
print(digits(1000))
print(digits(0))

# 4


def multiplication_table2(start, stop):
    for x in range(1, 4):
        for y in range(1, 4):
            print(str(x * y), end=" ")
        print()


multiplication_table2(1, 3)


# 5
def counter(start, stop):
    x = start
    if x > stop:
        return_string = "Counting down: "
        while x >= stop:
            return_string += str(x)
            if x != stop:
                return_string += ","
            x -= 1
    else:
        return_string = "Counting up: "
        while x <= stop:
            return_string += str(x)
            if x != stop:
                return_string += ","
            x += 1
    return return_string


print(counter(1, 10))
print(counter(2, 1))
print(counter(5, 5))


# 6
def even_numbers(maximum):
    return_string1 = ""
    for z in range(2, maximum+1):
        if z % 2 == 0:
            return_string1 += str(z)
    return return_string1


print(even_numbers(6))
print(even_numbers(10))
print(even_numbers(1))
print(even_numbers(3))
print(even_numbers(0))

# 8
for k in range(1, 10, 3):
    print(k)

# 9
for m in range(10):
    for n in range(m):
        print(n)

# 10


def votes(params):
    for vote in params:
        print("Possible option: " + vote)
