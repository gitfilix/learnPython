text = "We are going to have six methods today"
result = text.split("i")
print(result)

replaced = text.replace('six', 'a lot of')
print(replaced)

# join
a = "learning"
b = "Python"
c = "is"
d = "amazing"
e = " ".join([a, b, c, d])
print(e)

word_list = ["Simple","is","better","than","complex."]
all_words = " ".join(word_list)

# string = word_list.join(" ")
print(all_words)