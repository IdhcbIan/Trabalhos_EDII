import sys
import json
import subprocess
from multiprocessing import Pool

#----// Getting input //----------------------------

input_a = sys.stdin.read()
arr = json.loads(input_a)

def run_process(process_info):
    process, arr = process_info
    input_a = json.dumps(arr)
    result = subprocess.run(['python3', process], input=input_a, capture_output=True, text=True)
    output_a = json.loads(result.stdout)
    return output_a

#----// Splitting in two //----------------------------

if len(arr) > 1:
    L = []
    R = []
    mid = len(arr) // 2


    for i in range(mid):
        L.append(arr[i])

    for i in range(mid, len(arr)):
        R.append(arr[i])


#----// Creating Subprocesses //----------------------------

    processes = [('son.py', L), ('son.py', R)]

    if __name__ == '__main__':
        with Pool(processes=2) as pool:
            results = pool.map(run_process, processes)
        L, R = results




#----// Merging the Recursive output //----------------------------
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

#----// Printing the final output //----------------------------
    print(json.dumps(arr))

else:
#----// Stop Condition //----------------------------
    print(json.dumps(arr))
