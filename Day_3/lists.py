

my_list = ['a', 'b', 'c']

# from index 0 to 1 -> ['a'] because the index 1 is not included.
result = my_list[0:1]
# from index 0 to 2 -> ['a', 'b'] because the index 2 is not included.
result = my_list[0:2]
# all elements from 0 to end of list
result = my_list[0:]


my_list2 = ['d', 'e', 'f']
my_list3 = my_list + my_list2
my_list3.append('g')
# delete the first element
deleted = my_list3.pop(0)

print(my_list3)
print('deleted item at pos 0:'+ deleted)

my_list4 = ['g', 'a', 'b', 'c', 'o']
my_list4.sort()
print(my_list4)

my_list5 = ['y', 'e', 'z']
my_list5.reverse()
print(my_list5)
