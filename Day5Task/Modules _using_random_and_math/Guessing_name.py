'''5.  Create a Number Guessing Game where: 
● The program generates a random number between 1 and 50 using random. 
● The user has 5 attempts to guess the number.
● After each guess, calculate the absolute difference using math.fabs() and 
display how far the guess is from the correct number.
'''

import random
import math
number=random.randint(1,50)
print("Welcome to Number guessing Game!")
print("Guess a number between 1 and 50")
print("You have 5 attempts")
for i in range(1,6): #Gives u the 5 attempts
    guess=int(input("Enter your guess number ="))
    diff=math.fabs(number-guess)   # calculates the absolute difference between the correct number and guessed number
    print("Your guess is ",diff,"away from the correct number")
    if guess==number:
        print("Congrats its correct number")
        break
    elif guess < number:
        print("Number is too low")
    else:
        print("Number is to high")
else:
    print("Yoy have used all 5 attempts")
    print("the correct number is :",number)
