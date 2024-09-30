n = int(input())
dict = {}
for i in range(n):
    name, action = input().strip().split()
    dict[name] = action

result = [key for key, value in dict.items() if value == "enter"]
for name in sorted(result, reverse=True):
    print(name)
