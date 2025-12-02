import numpy as np

# Scalar Arithmatic 

array = np.array([1,2,3])

print(array + 1)
print (array - 2)

# Vecotrised math functions

array2 = np.array([1.01,2.5,3.99])

print(np.sqrt(array2))
print(np.round(array2))
print(np.floor(array2))

# Element Wise arithmetic 
print(array + array2)

# Broadcasting 

array3 = np.array([[1,2,3,4]])
array4 = np.array([[1],[2],[3],[4]])

print("Array 3 Shape:", array3.shape)
print("Array 4 Shape:", array4.shape)

print("Broadcast of array 3 and 4", array3 * array4)

# Numpy Functions 

array5 = np.zeros((2,10)) # there is a simmilar ones() function
print (array5)

array6 = np.full((2,10),9)
print (array6)

array7 = np.eye(3)
print ( array7)

array8 = np.arange(0,10)
print (array)

