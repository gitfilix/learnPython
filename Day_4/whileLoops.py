name = input("your name: ")

for letter in name:
    if letter == 'r':
        # break
        continue
    print(letter)


coins = 5
while coins > 0:
     print(f"I have {coins} coins")
     coins = coins -1

# Create a While Loop that subtracts one by one the numbers from 50 to 0 with the following additional conditions:
# If the number is divisible by 5, show that number on the screen
number = 50
while number > -1:
    if number / 5 % 1 == 0:
        print(number)
    number = number -1


# interrupt the flow when a negative number is occuring
list_numbers = [4, 5, 8, 7, 6, 9, 8, 2, 4, 5, 7, 1, 9, 5, 6, -1, -5, 6, -6, -4, -3]

for numbers in list_numbers:
    if numbers < 0:
        break;
    print(numbers)
