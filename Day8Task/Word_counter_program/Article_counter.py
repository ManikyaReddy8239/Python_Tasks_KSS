'''5. Word Counter Program 
A writer saves an article in a file called article.txt.
Write a Python program that: 
● Opens and reads the file 
● Counts the number of words, lines, and characters in the file 
● Displays the results.'''

file=open("article.txt","r")
data=file.read()
file.close()
words=data.split()
lines=data.splitlines()
characters=len(data)
print("\nThe articles is:")
print(data)
print("\nWord Count:",len(words))
print("Line Count:",len(lines))
print("Character Count:",characters)
