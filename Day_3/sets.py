# first notation of set
my_set = set((1, 2, 3, 4, 1, 3, 4, 2))
# all duplicated values are removed by python - {1, 2, 3, 4}
print(my_set)
# length of unique items
print(len(my_set))
# test if value is in set:
print(2 in my_set)

#combine sets
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = s1.union(s2)
# duplicate value '3' will be removed in s3
print(s3)

s1.add(8)
s1.remove(3)
# discard works like remove but no error if the element is not present
s1.discard(6)

print(s1)
# pop removes a RANDOM element
draw = s2.pop()
print('draw is: ',draw)


