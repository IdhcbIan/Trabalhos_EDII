import subprocess
import time
"""
name = input("Enter the name of the file: ")
num_tests = int(input("Enter the number of tests: "))
file_in = int(input("Enter first name of in file: "))
"""
name = 'run'
num_tests = 10000
file_in = 2

def run_and_count(name, num_tests, file_in):
    main = []

    file_in = str(file_in) + ".in"
    print(file_in)
    with open(file_in, 'r') as file:
        input_data = file.read()

    for i in range(num_tests):
        start_time = time.time()
        subprocess.run(['python3', name], input=input_data, text=True, capture_output=True)
        elapsed_time = time.time() - start_time 
        main.append(elapsed_time)
        average = sum(main) / len(main)
        return average


for i in range(0, 5):
    print("----------------------------------")
    print("For the file:" + str(file_in + i*4) + ".in")
    print("The average is:", run_and_count(name, num_tests, (file_in + 4*i)))


