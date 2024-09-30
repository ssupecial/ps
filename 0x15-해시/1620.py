n, m = list(map(int, input().split()))
names_list = [""] * (n + 1)
names_dict = {}

for i in range(1, n + 1):
    name = input().strip()
    names_list[i] = name
    names_dict[name] = i

for i in range(m):
    value = input().strip()
    if value.isalpha():
        print(names_dict[value])
    else:
        print(names_list[int(value)])
