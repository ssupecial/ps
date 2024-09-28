n = int(input())
arr = list(map(int, input().split()))


def check(x):
    if x == 1:
        return False
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1

    return True


answer = sum(list(map(check, arr)))

print(answer)
