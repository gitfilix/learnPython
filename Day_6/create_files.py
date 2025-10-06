# open with write-permission
# if it does not exist, it will be created.
# new lines and linebreaks have to be added manually
file = open('test_1.txt', 'w')

file.write('I am the new line in text \n')
file.write('I am the second line here')
file.write('''
    appending more text in a without manual linebreaks
    with the 3-quotes method
''')
print()
file.close()

file2 = open('test_2.txt', 'w')
# writelines should acutually be named: write all strings without any spaces
file2.writelines(['hi', 'there', 'lets', 'talk'])

my_list2 = ['hi', 'there', 'lets', 'talk']

for w in my_list2:
    file2.writelines(w + '\n')

file2.close()
# append to a file with 'a' option
file2 = open('test_2.txt', 'a')
file2.write('adding this string as it is opened with a- option')

file2.close()


file = open("my_file.txt", "w")
file.write("New text")
file.close()
file = open("my_file.txt", "r")
print(file.read())


#append text
file = open('my_file.txt', 'a')
file.write('New login')
file.close()
file = open('my_file.txt', 'r')
print(file.read())