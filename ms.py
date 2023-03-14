def mergeSort(A):
    if len(A)>1:
        mid=len(A)//2
        L=A[:mid]
        R=A[mid:]
        print("L:",L);print("R:",R)
        mergeSort(L)
        mergeSort(R)
        i=j=k=0
        while i<len(L) and j<len(R):
            if L[i]<R[j]:
                A[k] = L[i]
                i+=1
            else:
                A[k]=R[j]
                j+=1
            k+=1
        while i<len(L):
            A[k]=L[i]
            i+=1
            k+=1
        while j<len(R):
            A[k]=R[j]
            j+=1
            k+=1
        return A





A = [5, 2, 1, 8, 4]
#print(A)
A1.sort()
mergeSort(A)
print(mergeSort(A))