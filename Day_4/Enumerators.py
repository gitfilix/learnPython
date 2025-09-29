# classic way access index and item value of a list
my_list = ['a', 'b', 'c', 'd']
index= 0

for item in my_list:
    print(index, item)
    index += 1


# enumerator way

for index, item in enumerate(my_list):
    print('enum way:',index, item)

# create a tuples out of the list
my_tuples = list(enumerate(my_list))
print(my_tuples)

#access the value of third key element of a tuple -> 'c'
print('value ', my_tuples[2][1])


list_names = ["Maverick", "Alice", "Madeline", "Hazel", "Jack", "Meadow", "Thomas", "Emily", "Mills"]

tuple_names = list(enumerate(list_names))

for index, names, in tuple_names:
    print('index, name', index, names)

m_names = [(index, name) for index, name in tuple_names if name.startswith('M')]
for index, item in m_names:
    print (index)