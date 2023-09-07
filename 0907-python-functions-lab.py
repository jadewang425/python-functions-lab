# Challenge 1
def sum_to(n):
    sum = 0
    for num in range(n):
        sum += num
    return sum + n

print(sum_to(10))

# Challenge 2
def largest(list):
    ln = 0
    for num in list:
        if num >= ln:
            ln = num
    return ln

print(largest([10, 4, 2, 231, 91, 54]))

# Challenge 3
def occurrences(str1, str2):
    return str1.count(str2)
print(occurrences('fleep floop', 'ee'))

# Challenge 4
def product(*args):
    result = 1
    for arg in args:
        result *= arg
    return result
print(product(4, 0.5, 5))

#bonus
def steps_to_zero(num):
    steps = 0
    while num > 0:
        if num % 2 == 0:
            num /= 2
        else:
            num -= 1
        steps += 1
    return steps

print(steps_to_zero(14))