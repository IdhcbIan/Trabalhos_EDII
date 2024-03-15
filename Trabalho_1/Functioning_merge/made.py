#This is a attempt of me to do a merge sort with no help!!



def order(L):
    if len(L) <= 1:
        return L 
    else:
        h = len(L)//2
        FH = L[:h]
        SH = L[h:]
        
        #print(FH)
        #print(SH)
        
        FH = order(FH)
        SH = order(SH)

        i = j = k = 0
        new = []

        while len(FH) > 0 or len(SH) > 0: 
            if FH[0] < SH[0] or len(SH) == 0:
                new.append(FH[0])
                FH.remove(FH[0])
            else:
                new.append(SH[0])
                SH.remove(SH[0])

            
        print(new)
        return new

A = [1,3,4,2]

order(A)
