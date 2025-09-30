def greet_person(name):
    '''
    this is a comment to document the function to understand what is this function doing.
    '''
    print('Hello '+ name)


greet_person('felix')


def multiply(number1, number2):
    total = number1 * number2
    return total


result = multiply(2, 40)
print(result)

# exponential is just '**'
def power(base, exp):
    result = base ** exp
    print(result)
    return result


power(3, 4)