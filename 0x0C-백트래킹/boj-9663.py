def queen(k):  # 행
    global n, num
    if k == n:
        num += 1
        return

    for i in range(n):
        if (not isused[i]) and (not isused1[k + i]) and (not isused2[k - i + n - 1]):
            isused[i] = True
            isused1[i + k] = True
            isused2[k - i + n - 1] = True
            queen(k + 1)
            isused[i] = False
            isused1[i + k] = False
            isused2[k - i + n - 1] = False


n = int(input())
num = 0

isused = [False] * n
isused1 = [False] * (2 * n - 1)  # x+y
isused2 = [False] * (2 * n - 1)  # y-x+n-1

queen(0)

print(num)
