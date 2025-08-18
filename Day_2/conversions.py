num1 = 30.4

print(num1)
print(type(num1))

# convert num1 to integer -> that means the value changes to 30
num2 = int(num1)

print(num2)
print(type(num2))


age = input("Tell my you age: ")
# converts to integer, because input of age is a string
age = int(age)
# now the calculation works
new_age = 1 + age

print(new_age)


num2 = 10
num2 = float(num2)
print(type(num2))