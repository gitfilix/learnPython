# file manipulation

my_file = open('test.txt')

# store all content of the file in a list

#
show = my_file.read()
# shows the first line
one_line = my_file.readline()
print(one_line)

# shows the second line with the same command repeated
one_line = my_file.readline()
# note all string-methods are applicable here
print(one_line.upper())

# loop over
for l in my_file:
    print(' the content: ', l)

my_file2 = open('test.txt')
all = my_file2.readlines()
all = all.pop()
print('all: is the last element as we popped out: ', all)

# always close when you have been done
my_file.close()
my_file2.close()


my_file = open('my_text.txt')

all_lines = my_file.readlines()
second_line = all_lines.pop(1)
print(second_line)