'''Q2: Develop a Python program for a small shop to process customer purchases. Store product 
names and prices in a dictionary, items added to the cart in a list, product categories in a set, 
and product details using tuples. Create functions to display products, add items to the cart, and 
calculate the total bill. Use a recursive function to compute the total price of all items in the cart. 
Include exception handling to manage ValueError (invalid quantity input), ZeroDivisionError 
(calculation errors), TypeError (wrong data types in the cart), and NameError (when a product 
name entered by the user does not exist). 
Example Output: 
1. Display Products 
2. Add Item to Cart 
3. View Total Bill 
4. Exit 
Enter choice: 1 
Available Products: 
Pen : 10 
Notebook : 50 
Pencil : 5 
1. Display Products 
2. Add Item to Cart 
3. View Total Bill 
4. Exit 
Enter choice: 2 
Enter product name: Pen 
Enter quantity: 3 
Item added to cart successfully. 
1. Display Products 
2. Add Item to Cart 
3. View Total Bill 
4. Exit 
Enter choice: 2 
Enter product name: Notebook 
Enter quantity: 2 
Item added to cart successfully. 
1. Display Products 
2. Add Item to Cart 
3. View Total Bill 
4. Exit 
Enter choice: 3 
Items in Cart: 
Pen x 3 
Notebook x 2 
Total Bill: 130 
Example Exception Outputs 
ValueError 
Enter quantity: abc 
Invalid quantity! Please enter a number. 
NameError 
Enter product name: Eraser 
Product not found in store. 
TypeError 
Cart data type error. 
ZeroDivisionError 
Calculation error: division by zero.'''


products={"Pen":10,"NoteBook":50,"Pencil":5}
categories={"Stationery","Writing","Paper"}
product_details=(("Pen",10,"Stationery"),("Notebook",50,"Paper"),("Pencil",5,"Writing"))
cart=[]
#function to display products
def display_products():
    print("Available Products:")
    for name,price in products.items():
        print(name,":",price)
#function 2. add item to cart
def add_to_cart():
    name=input("Enter product name:")
    try:
        if name not in products:
            raise NameError
        quantity=int(input("Enter quantity:"))
        if quantity <= 0:
            print("Quantity must ne greater than zero")
            return
        cart.append((name,quantity))
        print("Item added to cart sucessfully")
    except ValueError:
        print("Invalid quantity please enter a number")
    except NameError:
        print("Product not found in store")

#Function 3.Recursive function to calculate total
def calculate_total(cart,index=0):
    #Base condition
    if index == len(cart):
        return 0
    item=cart[index]
    if not isinstance(item,tuple)or len(item) !=2:
        raise TypeError
    name,quantity=item
    if not isinstance(name,str) or not isinstance(quantity,int):
        raise TypeError
    price=products[name]
#recursive condition
    return(price*quantity)+calculate_total(cart,index+1)
#Function 4. Calculate total bill
def view_bill():
    try:
        print("Items in cart:")
        for name,quantity in cart:
            print(name,"x",quantity)
        if len(cart)==0:
            raise ZeroDivisionError
        total=calculate_total(cart)
        print("Total bill:",total)
    except ZeroDivisionError:
        print("Calculation error:division by zero")
    except TypeError:
        print("Cart data type error")
    except KeyError:
        print("Product data not found")

#Main menu
while True:
    print("\n1.Display Products")
    print("2. Add Item to Cart")
    print("3. View Total Bill")
    print("4. Exit")
    try:
        choice=int(input("Enter choice:"))
        if choice==1:
            display_products()
        elif choice==2:
            add_to_cart()
        elif choice==3:
            view_bill()
        elif choice==4:
            print("Thank you for shopping")
            break
        else:
            print("Invalid choice please try again")
    except ValueError:
        print("Please enter a valid numeric choice")
