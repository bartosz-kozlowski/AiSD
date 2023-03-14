def counting_sort(A):
    k = max(A)  # Find the maximum element in the list A

    C = [0] * (k + 1)
    B = [0] * len(A)

    for i in range(len(A)):
        C[A[i]] += 1
    for j in range(1, k + 1):
        C[j] += C[j - 1]
    print(C)
    for i in range(len(A) - 1, -1, -1):
        B[C[A[i]] - 1] = A[i]
        C[A[i]] -= 1

    return B
A = [5, 1, 4, 2, 8, 9]
print(A)
print(counting_sort(A))
