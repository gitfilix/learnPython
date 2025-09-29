# old way
word = 'feliks'
my_list = []

for letter in word:
    my_list.append(letter)
print(my_list)

# same with list comprehensions: do the loop inside
my_comp_list = [letter for letter in 'feliks']
print(my_comp_list)

# in a list every second element from 0 to 20
my_list = [n for n in range(0, 21, 2)]
print(my_list)

# operations within the same list:
my_half_list = [n / 2 for n in range(0, 21, 2)]
print(my_half_list)

# condition if n * 2 greater then 10 -> 6 is the first number meeting this condition.
my_list_condition = [n for n in range(0, 21, 2) if n * 2 > 10]
print(my_list_condition)

# second condition with else: print 'nope' if the first condition is not met:
my_list_two_condition = [n if n * 2 > 10 else 'nope' for n in range(0, 21, 2)]
print(my_list_two_condition)

# multiply
feet = [10, 20, 30, 40, 50]
meters = [f *0.3048 for f in feet]
print(meters)

values = [1, 2, 3, 4, 5, 6, 9.5]
square_values = [v * v for v in values]

# only even numbers
values2 = [1, 2, 3, 4, 5, 6, 9.5]
even_values = [v for v in values2 if v % 2 == 0]
print('even_values', even_values)


temperature_fahrenheit = [32, 212, 275]
degrees_celsius = [(((f -32) * 5) / 9) for f in temperature_fahrenheit]
print(degrees_celsius)