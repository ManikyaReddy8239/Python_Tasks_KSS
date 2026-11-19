'''13. Secure Login System (Decorators) 
A web application wants to ensure that users are authenticated before accessing 
sensitive functions.
Create a decorator that checks whether the user is logged in before 
allowing access to a function.'''

def login_required(func):
    def wrapper(is_logged_in):
        if is_logged_in:
            print("Login successfull")
            func()
        else:
            print("Access denied ! please login first")
    return wrapper
@login_required
def dashboard():
    print("Welcome to the Dashboard")
dashboard(True)
dashboard(False)
