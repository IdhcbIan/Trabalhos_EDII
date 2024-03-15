import sys
import json
import subprocess
from multiprocessing import Pool

arr = [3, 4, 2, 1, 6, 5, 8, 7, 10, 9]

processes = [('son.py', arr)]

def run_process(process_info):
    process, arr = process_info
    input_a = json.dumps(arr)  
    result = subprocess.run(['python3', process], input=input_a, capture_output=True, text=True)
    output_a = json.loads(result.stdout)
    return output_a

if __name__ == '__main__':
    with Pool(processes=1) as pool:
        results = pool.map(run_process, processes)
    print(results)
