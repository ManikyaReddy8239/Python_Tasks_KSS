'''Frequency Counter: Given a string `"programming"`,
create a dictionary that counts how many times each character appears.
 
    Expected output:
 
    ```python
    {'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1,
     'm': 2, 'i': 1, 'n': 1}'''

a="programming" #we are storing the word in variable a
b={}    # creating an empty set to store the lettere and their counts
for i in a:
    if i in b:
        b[i]+=1    #increase count by 1
    else:
        b[i]=1 
print(b)

