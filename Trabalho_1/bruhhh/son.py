import sys
import json
import subprocess
from multiprocessing import Pool

input_str = sys.stdin.read()
arr = json.loads(input_str)


if len(arr) > 1:

    mid = len(arr) // 2

    L = arr[:mid]
    R = arr[mid:]

    merge_sort(L)

    merge_sort(R)

processes = [('son.py', L), ('son.py', R)]

def run_process(process_info):
    process, array = process_info
    input_str = json.dumps(array)  
    result = subprocess.run(['python3', process], input=input_str, capture_output=True, text=True)
    output_array = json.loads(result.stdout)
    return output_array

if __name__ == '__main__':
    pool = Pool(processes=2)
    results = pool.map(run_process, processes)

    results[0] = L
    results[1] = R


i = j = k = 0

while i < len(L) and j < len(R):
    if L[i] < R[j]:
        arr[k] = L[i]
        i += 1
    else:
        arr[k] = R[j]
        j += 1
    k += 1

while i < len(L):
    arr[k] = L[i]
    i += 1
    k += 1

while j < len(R):
    arr[k] = R[j]
    j += 1
    k += 1


print(json.dumps(arr))
