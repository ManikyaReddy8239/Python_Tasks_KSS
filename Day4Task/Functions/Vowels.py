#19. Write a function that takes a string as input and returns the number of vowels.

def count_vowels(a):
    count=0
    for i in a:
        if i in "aeiouAEIOU":
            count=count+1
    return count
a=input("Enter a string :")
res=count_vowels(a)
print("Number os vowels=",res)
