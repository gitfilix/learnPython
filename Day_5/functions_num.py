numbers = [1,2,15,7,2,8]
def reduce_list(numbers):
    numbers = list(set(numbers))
    numbers.sort()
    numbers.pop(-1)
    return numbers
def average(numbers):
    avg_value = sum(numbers)/len(numbers)
    return avg_value


import random
secret_codes = [1,2,15,7,2,8]
def toss_coin():
    result = random.choice(["Heads", "Tails"])
    return result
def luck(coin, some_list):
    if coin == "Tails":
        print("List will self-destruct")
        return []
    elif coin == "Heads":
        print("List was saved")
        return some_list