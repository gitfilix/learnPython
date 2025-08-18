from Day_3.codeCallenge import firstLetter, lastLetter

text = input("enter a new text of your choice: ")
letters = []

text = text.lower()

letters.append(input('enter your 1. random character ').lower())
letters.append(input('enter your 2. random character ').lower())
letters.append(input('enter your 3. random character ').lower())


print("\n")
print("Letter repetition")

letter_repetition1 = text.count(letters[0])
letter_repetition2 = text.count(letters[1])
letter_repetition3 = text.count(letters[2])

print(f"We have fount the letter '{letters[0]}' repeated {letter_repetition1} times")
print(f"We have fount the letter '{letters[1]}' repeated {letter_repetition2} times")
print(f"We have fount the letter '{letters[2]}' repeated {letter_repetition3} times")

print("\n")
print("Number of words")

words = text.split()
print(f"We have found {len(words)} words in your text")

print("\n")
print("first and last characters")

firstLetter = text[0]
lastLetter = text[-1]

print('first letter is ', firstLetter)
print('last letter is ', lastLetter)

print("\n")
print("RE-verse the sentence")

words.reverse()
inverted_text = ' '.join(words)
print(f"reversed order of the words are: '{inverted_text}' ")

print("\n")
print("Looking for the word Python")

isPython = 'python' in text
#create a dictionary method -strange
dic = {True: 'was', False: 'was not'}

print(f"The word 'Python' {dic[isPython]} found tin the text")