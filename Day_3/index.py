my_text = "This text is a test"
# character at 7th position is: x
result = my_text[7]
print(result)
# substring search: at which position is word text starting? 5
result_index = my_text.index("text")
print(result_index)

# rindex: reverse index search from right to left - search for the last occurrence of 'practice'
sentence = "In theory, theory and practice are the same. In practice, they are not."
r_result = sentence.rindex("practice")
print(r_result)
