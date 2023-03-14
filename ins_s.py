def ins_sort(A):
    n = len(A)
    for i in range(1, n):
        key = A[i]
        j = i-1
        while j>=0 and A[j]>key:
            A[j+1] = A[j]
            j=j-1
        A[j+1]=key


A= [4, 5, 1, 3, 2]
ins_sort(A)
print(A)