minor = (min(45, 78, 64, 22))
major = (max(48, 46, 22, 79, 45, 88))

my_numbers = [8, 55, 12, 143, 12, 15, 77]

print(f'the biggest number it {max(my_numbers)} and the smallest number is {min(my_numbers)}')
# works also with strings ;-)
names = ['John', 'Felix', 'Sarah', 'Paul', 'Aron']
print(min(names))

#dictionary -> the lowest alphabetically value
dic = {'Key1': 33, 'Key2': 11, 'Key3': 30 }
#-> the lowest alphabetically value -> Key-1
print(min(dic))
# ->  for the value search:
print(min(dic.values()))
