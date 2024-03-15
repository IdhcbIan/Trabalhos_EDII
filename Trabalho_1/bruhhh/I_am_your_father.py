import sys
import json
import subprocess
from multiprocessing import Pool

arr = [3, 4, 2, 1, 6, 5]


processes = [('son.py', arr)]


def run_process(process_info):
    process, array = process_info
    input_str = json.dumps(array)  
    result = subprocess.run(['python3', process], input=input_str, capture_output=True, text=True)
    output_array = json.loads(result.stdout)
    return output_array

if __name__ == '__main__':
    pool = Pool(processes=1)
    results = pool.map(run_process, processes)

print(results)

