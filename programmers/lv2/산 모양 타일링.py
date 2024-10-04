# 17:20~


def solution(n, tops):
    notused = [0] * n
    used = [0] * n

    if tops[0] == 1:
        notused[0] = 3
    else:
        notused[0] = 2

    used[0] = 1

    for i in range(1, n):
        if tops[i] == 1:
            notused[i] = ((notused[i - 1] * 3) + (used[i - 1] * 2)) % 10007
        else:
            notused[i] = ((notused[i - 1] * 2) + (used[i - 1] * 1)) % 10007

        used[i] = (notused[i - 1] + used[i - 1]) % 10007

    answer = notused[n - 1] + used[n - 1]
    return answer


solution(4, [1, 1, 0, 1])
# solution(2, [0, 1])
