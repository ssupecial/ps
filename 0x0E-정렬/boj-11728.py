n, m = list(map(int, input().split()))
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
result = []

idx1 = 0
idx2 = 0

for i in range(n + m):
    if idx1 >= n:
        result.extend(arr2[idx2:])
        break
    elif idx2 >= m:
        result.extend(arr1[idx1:])
        break

    if arr1[idx1] > arr2[idx2]:
        result.append(arr2[idx2])
        idx2 += 1
    else:
        result.append(arr1[idx1])
        idx1 += 1

print(" ".join(map(str, result)))
