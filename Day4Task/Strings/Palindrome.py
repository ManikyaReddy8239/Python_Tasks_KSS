#8. Write a program to check whether a string is a palindrome.

a=input("enter a string :")
if a == a[::-1]:
    print("Its is a palindrome")
else:
    print("its not a palindrome")
