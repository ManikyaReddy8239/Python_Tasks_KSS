'''9. Online Shopping System (Multilevel Inheritance) 
An e-commerce company organizes products using multiple levels.
Create classes 
Product → ElectronicProduct → MobilePhone using multilevel inheritance and 
display product details.'''

class Product():
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def display_product(self):
        print("Product name:",self.name)
        print("Product Price:",self.price)
class ElectronicProduct(Product):
    def __init__(self,name,price,brand):
        self.name=name
        self.price=price
        self.brand=brand
    def display_electronic(self):
        print("Brand name:",self.brand)
class MobilePhone(ElectronicProduct):
    def __init__(self,name,price,brand,model):
        self.name=name
        self.price=price
        self.brand=brand
        self.model=model
    def display_mobile(self):
        self.display_product()
        self.display_electronic()
        print("Mobile model:",self.model)
obj=MobilePhone("Smartphone",25000,"Samsung","Galaxy S24")
obj.display_mobile()
