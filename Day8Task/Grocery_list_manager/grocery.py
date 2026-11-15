'''3. Grocery List Manager 
A user wants to save grocery items in a file grocery.txt.
Write a Python program that 
takes multiple items from the user and writes them into the file,
with each item on a new line. '''

file=open("grocery.txt","w")
n=int(input("Enter how many items do u want:"))
for i in range(n):
    item=str(input("Enter the grocery item:"))
    file.write(item + "\n")
file.close()
print("\nGrocery items saved successfully")
file=open("grocery.txt","r")
a=file.read()
print(a)
file.close()
