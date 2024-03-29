import time
import subprocess

name = input("Enter the name of the file: ")
num_tests = int(input("Enter the number of tests: "))
file_in = int(input("Enter first name of in file: "))

def run_and_count(name, num_tests, file_in):
    main = []

    file_in = str(file_in) + ".in"
    with open(file_in, 'r') as file:
        input_data = file.read()

    for i in range(num_tests):
        start = time.time()
        subprocess.run(['python3', name], input=input_data, text=True, capture_output=True)
        elapsed = time.time() - start 
        main.append(elapsed)
        average = sum(main) / len(main)
        return average


for i in range(0, 5):
    print("----------------------------------")
    print("For the file:" + str(file_in + i*4) + ".in")
    print("The average is:", run_and_count(name, num_tests, (file_in + 4*i)))


