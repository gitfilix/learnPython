names = ['hanna', 'Tony', 'sebastian']
ages = [65, 33, 12, 32]
cities = ['New york', 'Panama', 'Berlin', 'Bern']

combination = list(zip(names, ages, cities))
# print(combination)

for name, age, city in combination:
    print(f'{name} is {age} years old and lives in {city}.')
