'''4. Basic File Logger 
Scenario: 
A system logs user actions. 
Task: 
● Take user input 
● Store logs in a file 
● Use loop to allow multiple entries 
● Handle file errors using exception handling '''


try:
    file=open("user_logs.txt","a")
    while True:
        log=input("Enter user activity (or type exit):")
        if log.lower()=="exit":
            break
        file.write(log + "\n")
        print("Log saved successfully")
    file.close()
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")
except OSError:
    print("Error while handling file")
finally:
    print("Logging process completed")
