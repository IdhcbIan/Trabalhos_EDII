import subprocess
import time

main = []

name = input("Enter the name of the file: ")
num_tests = int(input("Enter the number of tests: "))

file_in = input("Enter name of in file: ")
file_in = file_in + ".in"
with open(file_in, 'r') as file:
    input_data = file.read()

for i in range(num_tests):
    start_time = time.time()
    subprocess.run(['python3', name], input=input_data, text=True, capture_output=True)
    elapsed_time = time.time() - start_time 
    main.append(elapsed_time)


print("----------------------------------")
print("The Times Where: ")
print("\n")
print(main)

print("\n")
print("----------------------------------")
print("\n")
average = sum(main) / len(main)
print("The average is:", average)

