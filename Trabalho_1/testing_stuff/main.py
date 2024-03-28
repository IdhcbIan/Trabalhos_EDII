#This is a attempt of me to do a merge sort with no help!!
def get_input():
    size = input()
    arr = [int(i) for i in input().split()]
    return arr
    


def order(arr):
    if len(arr) <= 1:
        return arr 
    else:
        h = len(arr)//2
        FH = arr[:h]
        SH = arr[h:]
        
        FH = order(FH)
        SH = order(SH)

        i = j = k = 0

        while i < len(FH) and j < len(SH):
            if FH[i] < SH[j]:
                arr[k] = FH[i]
                i += 1
            else:
                arr[k] = SH[j]
                j += 1
            k += 1

        while i < len(FH):
            arr[k] = FH[i]
            i += 1
            k += 1

        while j < len(SH):
            arr[k] = SH[j]
            j += 1
            k += 1

    return arr



main_arr = order(get_input())
print(*main_arr, sep=" ")
