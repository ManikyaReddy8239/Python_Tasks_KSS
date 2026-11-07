#4. Write a recursive function to reverse a string.
def reverse(s):
    if s == "":
        return s
    else:
        return reverse(s[1:]) + s[0]
name = input("Enter a string: ")
res= reverse(name)
print("Reversed string:",res)
