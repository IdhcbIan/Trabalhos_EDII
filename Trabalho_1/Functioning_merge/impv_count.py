import time
import subprocess

name = 'run'
num_tests = 10000
file_in = 2

def run_and_count(name, num_tests, file_in):
    input_filename = f"{file_in}.in"
    with open(input_filename, 'r') as file:
        input_data = file.read()

    elapsed_times = []
    for i in range(num_tests):
        start_time = time.perf_counter()
        result = subprocess.run(['python3', name], input=input_data, text=True, capture_output=True)
        if result.returncode != 0:
            print(f"Error in test {i}: {result.stderr}")
            continue  # Skip this iteration if there was an error
        elapsed_time = time.perf_counter() - start_time
        elapsed_times.append(elapsed_time)

    if elapsed_times:  # Avoid division by zero if all tests failed
        average = sum(elapsed_times) / len(elapsed_times)
    else:
        average = None  # or raise an exception
    return average

for i in range(0, 5):
    file_index = file_in + 4 * i
    print("----------------------------------")
    print(f"For the file: {file_index}.in")
    average_time = run_and_count(name, num_tests, file_index)
    if average_time is not None:
        print(f"The average time is: {average_time}")
    else:
        print("All tests failed.")
