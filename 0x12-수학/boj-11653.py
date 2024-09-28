def soinsu(x):
    i = 2
    answer = []
    while i * i <= x:
        while x % i == 0:
            print(i)
            x = x // i
        i += 1

    if x != 1:
        print(x)


n = int(input)
soinsu(1100)
