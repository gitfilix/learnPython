from random import shuffle

# initial list
sticks = ['-', '--', '---', '----']

# mixing sticks
def mix(my_list):
    shuffle(sticks)
    return (my_list)


# choose number
def try_your_luck():
    a_try = ''
    # we already have the numbers as strings as we a_try user input will be also a converted string
    while a_try not in ['1', '2', '3', '4']:
        a_try = input('choose a number: ')

    return int(a_try)


# check player try
def verify_try(a_list, a_try):
    # a_try list has index of 0, 1, 2, 3. so we reduce it by 1 and then
    if a_list[a_try -1] == '-':
        print('Looser today- wash the dishes tonight!')
    else:
        print("this time you are safe")

    print(f'You got {a_list}. and {a_try}')

mixed_sticks = mix(sticks)
selection = try_your_luck()
verify_try(mixed_sticks, selection)