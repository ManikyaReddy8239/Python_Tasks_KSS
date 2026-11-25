'''7. Generator-based Log Reader 
Scenario: 
A large log file needs to be processed. 
Task: 
● Create a generator to read file line by line 
● Use loop to process logs 
● Use condition to filter errors 
● Count occurrences using a dictionary'''


# Generator-based Log Reader

# 1. Create a sample log file
with open("application.log", "w") as file:
    file.write("INFO: Application started\n")
    file.write("ERROR: File not found\n")
    file.write("INFO: User logged in\n")
    file.write("ERROR: Database connection failed\n")
    file.write("ERROR: File not found\n")
    file.write("WARNING: Low memory\n")
    file.write("ERROR: Database connection failed\n")
    file.write("INFO: Application running\n")

# 2. Create a generator to read file line by line
def read_logs(filename):
    with open(filename, "r") as file:
        for line in file:
            yield line.strip()

# 3. Dictionary to count errors
error_count = {}

# 4. Use loop to process logs
print("All Log Messages:")

for log in read_logs("application.log"):

    print(log)

    # 5. Filter error messages using condition
    if "ERROR" in log:

        error = log.split("ERROR: ")[1]

        # 6. Count error occurrences using dictionary
        if error in error_count:
            error_count[error] += 1
        else:
            error_count[error] = 1

# 7. Display error counts
print("\nError Occurrences:")

for error, count in error_count.items():
    print(error, ":", count)
