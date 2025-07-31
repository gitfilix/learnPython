customer = {'name': 'John', 'last_name': 'Lennon', 'weight': 76, 'height': 1.78 }

query = (customer['height'])
print(query)

dic = {1: 33, 2: [10, 20, 34], 3:{'s1': 100, 's2': 200}}
print(dic[2][1])

dic2 = {'k1': ['a', 'b', 'c'], 'k2': ['d', 'e', 'f']}
#get the second key, second value and transform it uppercase
result = dic2['k2'][1].upper()
print(result)

#mutating key value pairs
dict3 = {1: 'a', 2: 'b'}

dict3[3] = 'c'

dict3[2] = 'Beta'
print(dict3)

# print keys
print(dict3.keys())

#print values
print(dict3.values())

#all content of the dictionary - tupples
print(dict3.items())
