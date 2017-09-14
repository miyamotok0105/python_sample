
list1 = ['1', '2', '3']
str1 = ''.join(list1)
print(str1)

list1 = [1, 2, 3]
str1 = ''.join(str(e) for e in list1)
print(str1)

L = ['L','O','L']
str1 = ''.join(map(str, L))
print(str1)
