'''6. Multi-Level List Transformation (Advanced List Comprehension) 
A dataset contains: 
data = [[1, 2, 3], [4, 5], [6]] 
Task: 
● Flatten the list using list comprehension. 
● Then create a new list containing squares of only even numbers.'''

data = [[1, 2, 3], [4, 5], [6]]
#flattened the nested list
flattened=[num for sublist in data for num in sublist]
#Find squares of even numbers only
even_square=[num ** 2 for num in flattened if num %2==0]
print("Original data:",data)
print("Flattend list:",flattened)
print("Even numbers square:",even_square)
