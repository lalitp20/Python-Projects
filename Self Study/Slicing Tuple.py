x = (1, 2, 3, 4, 5, 6, 7, 8, 9)
 
# Slicing the Tuple using two indexes
a = x[2:6] 
print("Both Indexes = ", a)
 
# Slicing the Tuple using First indexes
b = x[:6] 
print("No First Index = ", b)
 
# Slicing the Tuple using Second indexes
c = x[2:] 
print("No Second Index = ", c)
 
# Slicing the Tuple without using two indexes
d = x[:] 
print("No Indexes = ", d)
 
# Slicing the Tuple using Negative indexes
e = x[-3:] 
print("Negative First Index = ", e)
 
# Slicing the Tuple using Negative indexes
f = x[:-2] 
print("Negative Second Index = ", f)
