n = int(input())
dps = [0] * (n + 1)
dps[0] = 0
dps[1] = 0

for i in range(2, n + 1):
    if i % 6 == 0:
        dps[i] = min(dps[i // 2], dps[i // 3], dps[i - 1]) + 1
    elif i % 3 == 0:
        dps[i] = min(dps[i // 3], dps[i - 1]) + 1
    elif i % 2 == 0:
        dps[i] = min(dps[i // 2], dps[i - 1]) + 1
    else:
        dps[i] = dps[i - 1] + 1
print(dps[n])
