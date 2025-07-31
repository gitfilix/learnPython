# string properties

name = "Harry"

string_with_lineBreak = """This string has
linebreaks and they are 
possible due the 3 (double-) qoutes.
(3 singlequotes are also possible)"""

print(string_with_lineBreak)

# test if 'linebreaks' are into the string
print("linebreaks"  in string_with_lineBreak)
# test if not in string
print("sun" not in string_with_lineBreak)