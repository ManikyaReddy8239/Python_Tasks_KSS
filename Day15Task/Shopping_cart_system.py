'''3. Shopping Cart System 
Scenario: A user adds items to a shopping cart. 
Task: 
● Store items in a list 
● Convert to set to remove duplicates 
● Use loop + condition to calculate total cost 
● Handle invalid input using try-except'''

cart=[]
print("Available products:")
print("1.Pen - Rs.10")
print("2.NoteBook - Rs.50")
print("3.Pencil - Rs.5")
print("4.Eraser- Rs.10")
try:
    n=int(input("Enter the items how many u want to add:"))
    for i in range(n):
        item=str(input("Enter the item name:").lower())
        if item == "pen":
            cart.append(("Pen",10))
        elif item == "notebook":
            cart.append(("NoteBook",50))
        elif item == "pencil":
            cart.append(("Pencil",5))
        elif item == "eraser":
            cart.append(("Eraser",10))
        else:
            print("Invalid product")
    unique=set(cart)
    print("Shopping cart:")
    print(unique)
    total = 0
    for item,price in unique:
        if price > 0:
            total +=price
    print("Total Cost: Rs.",total)
except ValueError:
    print("Invalid input Please enter a valid number:")
except TypeError:
    print("Invalid data type")
