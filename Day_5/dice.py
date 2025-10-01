from random import *

def throw_dice():
    dice1 = randint(1, 6)
    print('dice1:', dice1)

    dice2= randint(1, 6)
    print('dice2:', dice2)
    return dice1, dice2


def roll_result(dice1, dice2):
    sum_dice = dice1 + dice2
    print('sum_dice', sum_dice)
    if sum_dice <= 6:
        print(f"The sum of your dice is {sum_dice}. Unfortunate")
    elif 6 < sum_dice < 10:
        print(f"The sum of your dice is {sum_dice}. You have a good chance")
    elif sum_dice >= 10:
        print(f"The sum of your dice is {sum_dice}. It looks like a winning roll")

dice1, dice2 = throw_dice()
roll_result(dice1, dice2)
