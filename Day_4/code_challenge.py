from random import *
userName = input('what is your name?: ')
tries = 8
print(f' okay {userName}! you have {tries} to figure out a number between 1 and 100')

secretNumber = int(randint(1, 100))

print('hint SecretNumber is', secretNumber)

while tries > 0:
    userNumber = int(input(f'you have {tries} guesses. Tryp to guess the SecretNumber '))
    if userNumber >= 101 or userNumber < 1:
        print('the number is out of range between 1 and 100')
        tries = tries -1
        print('tries left now', tries)
        continue
    if userNumber < secretNumber:
        print('the Secret number is bigger')
        tries = tries -1
        print('tries left', tries)
        continue
    if userNumber > secretNumber:
        print('your number is bigger then the Secret number')
        tries = tries -1
        print('tries left', tries)
        continue
    if userNumber == secretNumber:
        print(f'Yes! thats correct! you have won! you used {7 - tries} attempt to figure it out' )
        break

if tries == 0:
    print(f'Sorry, we have run out of attempts. Game over. you lost! the secret number was: {secretNumber}')


