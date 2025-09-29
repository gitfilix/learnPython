from random import *

my_random = randint(1, 50)
print(my_random)
# round up after 2 decimals
my_uni = round(uniform(1,  7), 2)
print(my_uni)

# orginal random is a float number
my_float_random = random()
print(my_float_random)

# choice: random from a list
colors = ['blue', 'green', 'red', 'yellow']
my_random_color = choice(colors)
print(my_random_color)

# shuffle method
numbers = list(range(5, 60, 5))
# changing the numbers randomly
shuffle(numbers)
print(numbers)

