my_list = ['a', 'b', 'c', 'd']

for letter in my_list:
    #indexnumber for each elment +1
    letter_number = my_list.index(letter) + 1
    print(f"letter {letter_number}: {letter}")


my_names = ['Paul', 'John', 'Felix', 'Kurt', 'Laura']

for name in my_names:
    if name.startswith('L'):
        print(name)

my_numbers = [1, 2, 3, 4, 5]
my_value = 0

for number in my_numbers:
    my_value = my_value + number

print(my_value)


word = 'python'

for characters in word:
    print(characters)


# with two assigned variables
for a, b in [[1, 2], [3, 4], [5, 6]]:
    print('a', a)
    print('b', b)


# in a dictionary
dic = {'key1': 'a', 'key2': 'b', 'key3': 'c'}

# whole item key value pair
for item in dic.items():
    print('item', item)

# values in dictionaries
for item in dic.values():
    print('values only', item)


list_numbers = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]

sum_numbers = 0
for number in list_numbers:
    sum_numbers = sum_numbers + number
print('sum_numbers', sum_numbers)



list_numbers = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]

sum_even = 0
for num in list_numbers:
    if num % 2 == 0:
        sum_even += num

print('sum_even', sum_even)
sum_odd = 0
for num in list_numbers:
    if num % 2 == 1:
        sum_odd += num