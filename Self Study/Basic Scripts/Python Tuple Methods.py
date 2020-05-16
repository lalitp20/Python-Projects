Fruits = ('Apple', 'Orange', 'Banana', 'Kiwi', 'Grape', 'Blackberry')
x = (9, 4, -5, 0, 22, -1, 2, 14)
 
#Finding Sum of all item in a Tuple using Python Sum() Method
print('Sum of all items in a x Tuple = ', sum(x))
 
#Calculating Length of a Tuple using Python len() Method
print('Length of a Fruits Tuple = ', len(Fruits))
print('Length of a x Tuple = ', len(x))
 
#Finding Minimum item in a Tuple using Python min() Method
print('Minimum item in a Fruits Tuple = ', min(Fruits))
print('Minimum item in a x Tuple = ', min(x))
 
#Finding Maximum item in a Tuple using Python max() Method
print('Maximum item in a Fruits Tuple = ', max(Fruits))
print('Maximum item in a x Tuple = ', max(x))
 
# Sorting the Tuple using Python Sorted() Method
print('After Sorting Fruits Tuple = ', sorted(Fruits))
print('After Sorting x Tuple = ', sorted(x))
 
# Index position of an item in a Tuple using Python index() Method
print('The Index position of Banana = ', Fruits.index('Banana'))
print('The Index position of -1 = ', x.index(-1))
 
# Counting items in a Tuple using Python count() Method
y = (9, 4, 1, 4, 9, -1, 2, 4)
print('Number of Times 4 is repeated = ', y.count(4))
print('Number of Times 9 is repeated = ', y.count(9))
 
# Converting List into Tuple
z = [1, 2, 3, 4, 5]
print(tuple(z))
