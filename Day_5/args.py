def a_sum(*args):
    total = 0
    for arg in args:
        total += arg

    return total

def b_sum(*args):
    return sum(args)

result = a_sum(2, 4, 23, 2)
print('b_sum:', b_sum(2, 4, 1, 2))
print('a_sum result', result)


def sum_squares(*args):
    total = 0
    for n in args:
        n = n * n
        total = total + n

    return total


result = sum_squares(1, 2, 4, 6)

print('result squares', result)

# convert all negative numbers to positive values
def absolute_sum(*args):
    positive_numbers = list(map(abs, args))
    total = sum(positive_numbers)

    return total


result = absolute_sum(2, 4, -2, -5, 6, -32)
print('result absolute positive numbers', result)


def personal_numbers(name, *args):
    sum_numbers = sum(args)
    return f"{name}, the sum of your numbers is {sum_numbers}"