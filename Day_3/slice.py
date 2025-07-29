text = "ABCDEFGHIJKLM"
# slice the fragment from index 2 to 5
fragment1 = text[2:5]
print(fragment1)

# slice the fragment form start to 7
fragment2 = text[:7]
print(fragment2)

# slice the fragment form 4 to the end
fragment3 = text[4:]
print(fragment3)

#slice the fragment: start from pos 2 to 10 (not include 10), then take every second character (last parameter): CEGI
fragment4 = text[2:10:2]
print(fragment4)

#take all and reverse it
fragment5 = text[::-1]
print(fragment5)

#take every second and reverse it
fragment6 = text[::-2]
print(fragment6)