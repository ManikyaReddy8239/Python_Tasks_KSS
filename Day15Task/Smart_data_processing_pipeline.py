'''9. Smart Data Processing Pipeline 
Scenario: 
A system processes numeric data from file. 
Task: 
● Read numbers from a file 
● Use NumPy for calculations (mean, std) 
● Convert results to Pandas DataFrame 
● Use exception handling for bad data 
● Use a generator to stream data 
● Apply decorator to measure execution time 
'''


import numpy as np
import pandas as pd
import time

# 1. Create a sample file
with open("numbers.txt", "w") as file:
    file.write("10\n")
    file.write("20\n")
    file.write("30\n")
    file.write("abc\n")
    file.write("40\n")
    file.write("50\n")
    file.write("hello\n")

# 2. Create a decorator to measure execution time
def measure_time(func):

    def wrapper(*args, **kwargs):

        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()

        print("\nExecution Time:", end - start, "seconds")

        return result

    return wrapper


# 3. Create a generator to read numbers from file
def read_numbers(filename):

    with open(filename, "r") as file:

        for line in file:

            try:
                number = float(line.strip())
                yield number

            except ValueError:
                print("Invalid data skipped:", line.strip())


# 4. Apply decorator to processing function
@measure_time
def process_data():

    numbers = []

    # 5. Read data using generator
    try:
        for number in read_numbers("numbers.txt"):
            numbers.append(number)

    except FileNotFoundError:
        print("File not found!")
        return

    # Check whether valid numbers exist
    if not numbers:
        print("No valid numbers found!")
        return

    # 6. Convert into NumPy array
    arr = np.array(numbers)

    # 7. Calculate mean and standard deviation
    mean_value = np.mean(arr)
    std_value = np.std(arr)

    # 8. Convert results into Pandas DataFrame
    df = pd.DataFrame({
        "Calculation": ["Mean", "Standard Deviation"],
        "Result": [mean_value, std_value]
    })

    print("\nNumeric Data:")
    print(arr)

    print("\nData Analysis Results:")
    print(df)


# 9. Call the function
process_data()
