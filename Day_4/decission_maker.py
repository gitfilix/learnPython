pet = 'dog'

if pet == 'cat':
    print('you have a cat')
elif pet == 'dog':
    print('you have a dog')
else:
    print('dont know but its no cat and no dog')



age = 16
school_grade = 8

if age < 18:
    print('you are a teeny')
    if school_grade >= 7:
        print('passed')
    else:
        print('Failed')
else:
    print('you are an adult')

num1 = int(input("Enter a number:"))
num2 = int(input("Enter another number:"))

if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num2 > num1:
    print(f"{num2} is greater than {num1}")
elif num1 == num2:
    print(f"{num1} and {num2} are equal")


age = 16
has_license = False

if age >= 18 and has_license:
    print("You can drive")
elif age < 18:
    print("You can't drive yet. You must be 18 years old and have a license")
elif age > 18:
    if not has_license:
        print("You can't drive. You need to have a license")