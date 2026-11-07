#3. Write a recursive function to calculate the sum of digits of a number. 
#Example: Input = 123 → Output = 6

def sumdigits(n):
    if n == 0:
        return 0
    else:
        return(n % 10) + sumdigits(n // 10)
num=int(input("Enter a number :"))
res=sumdigits(num)
print("The sum of digits of a number : ",res)
