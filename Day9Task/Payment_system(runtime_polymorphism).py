'''11. Payment System (Runtime Polymorphism) 
An online store supports multiple payment methods: CreditCard, UPI, and 
NetBanking. Create a base class Payment with a method process_payment() and 
override it in each payment type.'''

class Payment:
    def process_payment(self):
        print("Processing payment")
class CreditCard(Payment):
    def process_payment(self):
        print("Payment through credit card")
class UPI(Payment):
    def process_payment(self):
        print("Payment through UPI")
class NetBanking(Payment):
    def process_payment(self):
        print("Payment through Netbanking")

n=NetBanking()
n.process_payment()
u=UPI()
u.process_payment()
c=CreditCard()
c.process_payment()
p=Payment()
p.process_payment()
