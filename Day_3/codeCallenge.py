# ask user for inserting text
userText = input('please enter a nice sentence with words: ')

# split string on ' ' and count the words of the string
userTextWordsCount = len(userText.split())
print('you wrote', userTextWordsCount, ' words in your text')

userTextWords = userText.split()

#first and last letter in the text
firstLetter = userText[0:1]
lastLetter = userText[-1]
print('first letter in the text is: ', firstLetter)
print('last letter in the text is: ', lastLetter)

# is word pyhon in it?
isPyhonPresent = bool('python' or 'Python' in userText)
print('is the word Python found ?', isPyhonPresent)

# ask for 3 random letters
randomLetter1 = input('please enter the first random Letter ')
randomLetter2 = input('please enter the second random Letter ')
randomLetter3 = input('please enter the third random Letter ')

# write randomLetters in a List
randomLetterList = [randomLetter1, randomLetter2, randomLetter3]
print('random letter list is ', randomLetterList)

checkRandomLetters = {letter: userText.count(letter) for letter in randomLetterList}
print('random letters appearing ', checkRandomLetters)

# count the total characters of userText
userTextLength = len(userText)

print('the length of the Text is: ', userTextLength,  'characters')

# inverted order of the words in the sentence
reversedWords = " ".join(userTextWords[::-1])
print('inverted order of the words are: ', reversedWords)