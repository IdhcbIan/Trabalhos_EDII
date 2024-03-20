import subprocess
import time  # Importing the time module

# Main list to store elapsed times
main = []

# User input for script name and number of tests
name = input("Enter the name of the file: ")
num_tests = int(input("Enter the number of tests: "))

# Run the specified number of tests
for i in range(num_tests):
    start_time = time.time()  # Record the start time
    subprocess.run(['python3', name], capture_output=True, text=True)  # Run the script
    elapsed_time = time.time() - start_time  # Calculate elapsed time
    main.append(elapsed_time)  # Add to the list of elapsed times

# Print the list of elapsed times
print(main)
