'''8. Decorator-based Access Control 
Scenario: 
Restrict access to certain functions. 
Task: 
● Create a decorator to check user role 
● Use condition inside decorator 
● Apply decorator to multiple functions 
● Store roles in a dictionary
'''


# Decorator-based Access Control

# 1. Store user roles in a dictionary
users = {
    "Alice": "admin",
    "Bob": "manager",
    "Charlie": "employee"
}

# Current logged-in user
current_user = "Alice"

# 2. Create a decorator
def check_role(required_role):

    def decorator(func):

        def wrapper():

            user_role = users[current_user]

            # 3. Check user role using condition
            if user_role == "admin" or user_role == required_role:
                print("Access Granted!")
                func()
            else:
                print("Access Denied! You don't have permission.")

        return wrapper

    return decorator


# 4. Apply decorator to multiple functions

@check_role("manager")
def view_reports():
    print("Viewing company reports...")


@check_role("admin")
def delete_records():
    print("Deleting records...")


@check_role("employee")
def view_profile():
    print("Viewing employee profile...")


# 5. Call functions
print("Current User:", current_user)

view_reports()

delete_records()

view_profile()
