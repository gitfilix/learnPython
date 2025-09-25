
# range from 20 to 30 (included) every 2nd step
for num in range(20, 31, 2):
    print(num)


#create a list from 1 to 100
my_list = list(range(1, 101))
print(my_list)

# sum of the squares of each number from range 1- 15
sum_squares = 0
for i in range(1, 16):
    print('sum_squares', sum_squares)
    sum_squares += i**2