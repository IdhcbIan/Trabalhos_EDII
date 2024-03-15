
╭━╮╭━╮╱╱╱╱╱╱╱╱╱╱╱╭━━━╮╱╱╱╱╭╮
┃┃╰╯┃┃╱╱╱╱╱╱╱╱╱╱╱┃╭━╮┃╱╱╱╭╯╰╮
┃╭╮╭╮┣━━┳━┳━━┳━━╮┃╰━━┳━━┳┻╮╭╯
┃┃┃┃┃┃┃━┫╭┫╭╮┃┃━┫╰━━╮┃╭╮┃╭┫┃
┃┃┃┃┃┃┃━┫┃┃╰╯┃┃━┫┃╰━╯┃╰╯┃┃┃╰╮
╰╯╰╯╰┻━━┻╯╰━╮┣━━╯╰━━━┻━━┻╯╰━╯
╱╱╱╱╱╱╱╱╱╱╭━╯┃
╱╱╱╱╱╱╱╱╱╱╰━━╯

#-----------------------------
#Made by chat gpt(go make ur own)

def merge_sort(arr):
    if len(arr) > 1:

        # Finding the mid of the array
        mid = len(arr) // 2

        # Dividing the array elements into 2 halves
        L = arr[:mid]
        R = arr[mid:]

        # Sorting the first half
        merge_sort(L)

        # Sorting the second half
        merge_sort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    return arr

# Test the function
arr = [12, 11, 13, 5, 6, 7]
sorted_arr = merge_sort(arr)
print("Sorted array is:", sorted_arr)
