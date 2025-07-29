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

