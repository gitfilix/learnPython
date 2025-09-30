

def check_3_digits(nlist):
    #check if there is a 3digit number in the list
    has_three = []
    for n in nlist:
        if n in range(100, 1000):
            has_three.append(n)
        else:
            pass

    return has_three


nlist = [343, 2, 12, 233]
result = check_3_digits(nlist)
print(result)




def all_positives(numbers):
    # check if all are positive else return false
    for n in numbers:
        if n < 0:
            return False

    return True

numbers = [12, -84, -5, 48, 77, 8]
result2 = all_positives(numbers)
print(result2)


def sum_less(numbers2):
    sum = 0
    for n in numbers2:
        if n in range(0, 1000):
            sum = sum + n
            print('sum now', sum)
        else:
            pass
    return sum

numbers2 = [13, 103, 223, 1, 4822, 32]
result2 = sum_less(numbers2)
print('result_less:', result2)


numbers3 = [1,50,502,5000,755,600,33,61]
def count_even(numbers3):
    count=0
    for number in numbers3:
        if number % 2 == 0:
            count += 1
        else:
            pass
    return count