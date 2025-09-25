### Phython is the BEST language to learn
(they say)

### Python is a high-level, interpreted, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including object-oriented, imperative, functional and procedural, and has a large and comprehensive standard library.


## backslash: ignore exactly the next character!  

mac combination for backslash 

`option-shift-7`


## concatinated functions
will be executed from inside-out

print(input("What's your name?") +" " + input("What's your surname?"))

first input-functions, then print-function.


Data Types in Python
--------------------

Integers: 1, 155, 0, -15
-> used for counting, indexing, ranking, days, 


Floats: 1.0, 155.0, 0.0, -15.5
-> used for decimal numbers: grades, values, weights

Booleans: True, False

Structures
----------

1. Lists: ["apple", "banana", "cherry", 2.0, 154, "mars" ]
(arrays in JS)
-> mutable, ordered, duplicate allowed

2. Dictionaries: {"name": "John", "surname": "Doe", "age": 30}
(key-value pairs, like a object in JS)
-> mutable, unordered, duplicate not allowed

3. Tuples: ("apple", "banana", "cherry", 2.0, 154, "mars" )
(immutable order! )
-> not mutable, ordered, duplicate not allowed

4. Sets: {"apple", "banana", "cherry", "mars" }
(list of UNIQUE elements)
-> not mutable, unordered, duplicate not allowed


Variables
---------
nameing restrictions:
- cannot start with a number
- cannot contain a space or hyphen
- are case-sensitive!
- cannot be a python keyword
- Symbols like ', < > / ? | \ ( ) ! @ # $ % ^ & *= - + ~ are not allowed


Type Casting 
----------------

Implicit: (automatic)
int(1.0) -> 1
float(1) -> 1.0
str(1) -> "1"


Explicit: (manually transformed)

int(1.0) -> 1
float(1) -> 1.0
str(1) -> "1"

to list:
my_list = list("hello")


String formatting
-------------------

1. format()
print("Hello, {} my number is {}".format("John", 1234567890))

2. literal string interpolation
print(f"Hello, {name} my number is {number}")

color = "red"
licence_plate = 343432

-> thats very readable literal string starting with 'f', modern way

print(f"The car is {color} and its licence plate is: {licence_plate}")


conversions to integer

sales = input("Enter sales amount: ")
sales = int(sales)


index method
-------------

my_text = "This text is a test"
# character at 7th position is: x
result = my_text[7]
print(result)
# substring search: at which position is word text starting? 5
result_index = my_text.index("text")
print(result_index)

# rindex: reverse index search from right to left - search for the last occurrence of 'practice'
sentence = "In theory, theory and practice are the same. In practice, they are not."
r_result = sentence.rindex("practice")
print(r_result)


slicing
-------
text = "ABCDEFGHIJKLM"
# slice the fragment from index 2 to 5
fragment1 = text[2:5]


# slice the fragment form start to 7
fragment2 = text[:7]


# slice the fragment form 4 to the end
fragment3 = text[4:]

# slice the fragment: start from pos 2 to 10 (not include 10), then take every second character (last parameter): CEGI
fragment4 = text[2:10:2]

# take all and reverse it
fragment5 = text[::-1]

# take every second and reverse it
fragment6 = text[::-2]


# Take every third character starting from the ninth to the end of the sentence, and print the result.
sentence = "Never trust a computer you can't throw out a window"
result = sentence[8::3]


# split strings

result.split("i") -> split on the character i
result.split() -> split on every space

# join
a = "learning"
b = "Python"
c = "is"
d = "fun!"
e = " ".join([a, b, c, d])
print(e)

word_list = ["Simple","is","better","than","complex."]
all_words = " ".join(word_list)


strings properties
--------------------
- is immutable
- is ordered
- is iterable

# length
len("hello") -> 5

word = "electroencephalographist"
print(len(word)) -> 24

# test if 'linebreaks' are into the string
print("linebreaks"  in string_with_lineBreak)
# test if not in string
print("sun" not in string_with_lineBreak)

lists properties
-----------------
- is mutable
- is ordered
- is iterable

my_list = ['a', 'b', 'c']

# from index 0 to 1 -> ['a'] because the index 1 is not included.
result = my_list[0:1]
# from index 0 to 2 -> ['a', 'b'] because the index 2 is not included.
result = my_list[0:2]
# from index 1 to 2 -> ['b', 'c'] because the index 2 is not included.
result = my_list[1:2]
# you get the point

# all elements from 0 to end of list
result = my_list[0:]

my_list = ['a', 'b', 'c']
# without parameters it will delete the last element!
my_list.pop()
# with parameter it will delete the element at the given index!
my_list.pop(1)


dictionaries properties
------------------------
- is mutable !
- is unordered
- is iterable
- no index (is unordered, and no index)

my_dict = {'name': 'John', 'surname': 'Smith'}


dic2 = {'k1': ['a', 'b', 'c'], 'k2': ['d', 'e', 'f']}
# get the second key, second value and transform it uppercase
result = dic2['k2'][1].upper()

# mutating key value pairs
dict3 = {1: 'a', 2: 'b'}

dict3[3] = 'c'

dict3[2] = 'Beta'
print(dict3)

# print keys
print(dict3.keys())

# print values
print(dict3.values())

# all content of the dictionary - tupples
print(dict3.items())

Tuples
-------
very similar to lists, but they are immutable!

my_tuple = (1, 2, (10, 20), 5, 2)

# count: how many times we have value 2?
print(my_tuple.count(2))

# index: at what position is value 5? - 3
print(my_tuple.index(5))


set
-----------------
- unordered !
- no index
- no duplicates

my_set = {1, 2, 3, 4, 5}
or:
(needs 2 brackets, no comma between brackets)
my_set = {1, 2, 3, 4, 5}
my_set = set([1, 2, 3, 4, 5])


# first notation of set
my_set = set((1, 2, 3, 4, 1, 3, 4, 2))
# all duplicated values are removed by python - {1, 2, 3, 4}
print(my_set)
# length of unique items
print(len(my_set))
# test if value is in set:
print(2 in my_set)

#combine sets
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = s1.union(s2)
# duplicate value '3' will be removed in s3
print(s3)

s1.add(8)
s1.remove(3)
# discard works like remove but no error if the element is not present
s1.discard(6)

print(s1)
# pop removes a RANDOM element
draw = s2.pop()
print('draw is: ',draw)


Booleans
--------

list = [1, 3, 4, 6]
control = 5 in list

print(type(control))
print(control)

test = bool(17834/34 > 87*56)
print(test)

Comparison Operators
--------------------

my_bool = 'white' == 'White' // false - case sensitive !

logical operators

keyword 'and' my_bool = 4 < 5 and  5 > 6
keyword 'or'   (one of the condition is true)
keyword 'in' for strings -> wordIsIn = 'sentence' in text
keyword 'not' for testing if a value is falsy


controll flow
-------------

if statements: if met -> good execute intended code, if not proceed.

elif: else if

age = 16
has_license = False

if age >= 18 and has_license:
    print("You can drive")
elif age < 18:
    print("You can't drive yet. You must be 18 years old and have a license")
elif age > 18:
    if not has_license:
        print("You can't drive. You need to have a license")


1. for-loops
---------------
my_numbers = [1, 2, 3, 4, 5]
my_value = 0

for number in my_numbers:
    my_value = my_value + number

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


2. while loop

 - we cannot know how many times the loop will be executed

while some_condition:
    #this code

else:
    #other_code execution

`number = 10
while number > -1:
    print(number)
    number = number - 1`

break: interrupt

continue:

pass: do nothing

# Create a While Loop that subtracts one by one the numbers from 50 to 0 with the following additional conditions:
# If the number is divisible by 5, show that number on the screen 
`
number = 50
while number > -1:
    if number / 5 % 1 == 0:
        print(number)
    number = number -1
`

3. ranges for integers only

# range from 20 to 30 (included) every 2nd step
for num in range(20, 31, 2):
    print(num)

# create a list from 1 to 100
my_list = list(range(1, 101))
print(my_list)
