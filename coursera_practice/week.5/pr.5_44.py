def merge(A, B):
    C = []
    i, j = 0, 0
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            C.append(A[i])
            i += 1
        elif A[i] > B[j]:
            C.append(B[j])
            j += 1
        else:
            C.append(A[i])
            i += 1
    C.extend(B[j:])
    C.extend(A[i:])
    return C


a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(*merge(a, b))
