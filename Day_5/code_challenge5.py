from random import *

words = ['alleycat', 'robocop', 'attack chopper', 'digger', 'oil imperium']
correct_letters = []
incorrect_letters = []
user_tries = 6
right_answers = 0
game_over = False

# print('secret:', secret)

def choose_word(list_of_words):
    chosen_word = choice(list_of_words)
    # different letters: how many letters are different from the words in a set and the length of
    # all not
    different_letters = len(set(chosen_word))
    print('-> secret chosen_word is: ', chosen_word)
    print('different letters', different_letters)
    return  chosen_word, different_letters


def ask_letter():
    chosen_letter = ''
    is_valid = False
    # check if the user added an input valid from the alphabet
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    while not is_valid:
        chosen_letter = input('Hey user, type a letter, please: ')
        # check if the input letter is only one length and from alphabet
        if chosen_letter in alphabet and len(chosen_letter) == 1:
            is_valid = True
        else:
            print('You have not entered a valid letter')

    return chosen_letter

#print the game progress
def show_new_board(chosen_word):
    hidden_list = []

    for l in chosen_word:
        if l in correct_letters:
            hidden_list.append(l)
        else:
            hidden_list.append('-')

    # output joined hidden list
    print(' '.join(hidden_list))


def check_letter(chosen_letter, hidden_word, user_tries, matches):
    # game status
    end = False
    # guess correct: if the letter is in secret word and not already in the correct letters
    if chosen_letter in hidden_word and chosen_letter not in correct_letters:
        correct_letters.append(chosen_letter)
        matches += 1
    # inform user that he already has the letter guessed - dont remove a try
    elif chosen_letter in hidden_word and chosen_letter in correct_letters:
        print("you already have guessed this letter and its correct")
    # wrong guess
    else:
        incorrect_letters.append(chosen_letter)
        user_tries -= 1
    # check if user_tries is 0
    if user_tries == 0:
        # call lose function
        end = lose()
    elif matches == unique_letters:
        # call win function
        end = win(hidden_word)

    return user_tries, end, matches


def lose():
    print('no tries left, you lost!')
    print(f'the secret word was: {word} ')
    # game over is true
    return True

def win(revealed_word):
    show_new_board(revealed_word)
    print(f'Yea you won!!! you guessed the correct word: {revealed_word}')
    # game over is true
    return True

# call choose_word with the secret words list:
# return the chosen_word = (word), different_letters: unique_letters
word, unique_letters = choose_word(words)

# while the game is not over: repeat these prints and
# show the board with
while not game_over:
    print('\n' + '*' * 20 + '\n' )
    show_new_board(word)
    print('\n')
    print('Incorrect letters: ' + '-'.join(incorrect_letters))
    print(f'Tries left:  {user_tries}')
    print('\n' + '*' * 20 + '\n')
    # store chosen-letter in letter here
    letter = ask_letter()
    # we store 3 variables: user_tries, over, right_answers
    user_tries, over, right_answers = check_letter(letter, word, user_tries, right_answers)
    game_over = over


