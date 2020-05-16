Fruits = ['Apple', 'Orange', 'Banana', 'Kiwi', 'Grape', 'Blackberry']
x = [9, 4, -5, 0, 22, -1, 2, 14]

Fruits.sort()
x.sort()
print(Fruits)
print(x)
 
# Reverse the List using Python reverse() Method
Fruits.reverse()
x.reverse()
print(Fruits)
print(x)
 
# Index position of an item in the List using Python index() Method
print('The Index position of Banana = ', Fruits.index('Banana'))
print('The Index position of -1 = ', x.index(-1))
 
# Counting items in the List using Python count() Method
y = [9, 4, 1, 4, 9, -1, 2, 4]
print('Number of Times 4 is repeated = ', y.count(4))
print('Number of Times 9 is repeated = ', y.count(9))
