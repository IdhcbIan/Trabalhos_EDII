import subprocess

def run_and_compare(name, file_in):
    result = "Fail"
    
    file_in_with_extension = f"{file_in}.in"
    file_out_with_extension = f"{file_in}.out"
    
    with open(file_in_with_extension, 'r') as file:
        input_data = file.read()
    
    with open(file_out_with_extension, 'r') as file:
        expected_output = file.read().strip()

    process_result = subprocess.run(['python3', name], input=input_data, text=True, capture_output=True)
    actual_output = process_result.stdout.strip()

    # Splitting both outputs by lines and stripping whitespace for comparison
    if actual_output.splitlines() == expected_output.splitlines():
        result = "Pass"

    return result

name = 'main'
file_in = 1

for i in range(0, 20):
    current_file_in = file_in + i
    print("----------------------------------")
    print(f"For the file: {current_file_in}.in")
    result = run_and_compare(name, current_file_in)
    print("Result:", result)
