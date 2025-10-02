
def a_sum(**kwargs):
    # kwargs is now a dictionary type
    print(type(kwargs))
    total = 0
    for key, value in kwargs.items():
        print(f'key', key, 'value', value)
        total += value

    return total


print(a_sum(x=2, y=4, z=7))

def test(number1, number2, *args, **kwargs):

    print(f'The value number1 is', {number1})
    print(f'The value number2 is', {number2})

    for arg in args:
        print(f'arg ={arg}')

    for key, value in kwargs.items():
        print(f'kwargs are key and value:{key} = {value}')


test(3, 22, 132, 133, 134, 135, x='please', y='show', z='me' )

# with args as variables in a list or pseudo key-value dictionary
args = [100, 200, 400]
kwargs = {'x': 'the title of x', 'y': 'the direction of y', 'z': 'how to get there'}
test(26, 3, *args, **kwargs)


# count the arguments
def number_attributes(**kwargs):
    totalargs = 0
    for key, value in kwargs.items():
        print('key', key)
        print('value', value)
        totalargs = totalargs + 1

    return totalargs


result = number_attributes(x='please', y='show', z='me', a='hi', b='there')
print('result', result)