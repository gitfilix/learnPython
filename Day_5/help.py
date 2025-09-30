dic = {'key1': 100, 'key2': 200, 'key3': 312}
# popitem() removes last element - key3 here
a = dic.popitem()
# update() changes a key - value or adds another key
b = dic.update({'key4':400})
c = dic.update({'key2': 202})

print('a', a)
print('b', b)
print('c', c)
print('dic now', dic)

# removes characters from the left side
string = ",:_#,,,,,,:::____##Total_ _Pyt%on,,,,,,::#"
string = string.lstrip(",:_#%")
print('string', string)

#insert a element in a string on the 4th position
fruits = ["mango", "banana", "cherry", "plum", "grapefruit"]
fruits.insert(3, "orange")
print(fruits)

# is disjoint method: check if the sets have  NO common elements. here "Samsung" is in both, so isdisjoint is false
phone_brands = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
tv_brands = {"Sony", "Philips", "Samsung", "LG"}

isolated_sets = phone_brands.isdisjoint(tv_brands)
print('isolated', isolated_sets)
