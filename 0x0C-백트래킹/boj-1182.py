# n, s = list(map(int, input().split()))
# numbers = list(map(int, input().split()))
# count = 0


# def func(depth, total):
#     global count
#     if depth == n:
#         if total == s:
#             count += 1
#         return
    
#     func(depth+1, total+numbers[depth]);
#     func(depth+1, total)

# func(0, 0)
# if s == 0:
#     count -= 1

# print(count)

n, s = list(map(int, input().split()))
numbers = list(map(int, input().split()))
count = 0
arr = []


def func(depth):
    global count

    if depth == n:
        if len(arr) != 0 and sum(arr) == s:
            count += 1
        return
    
     
    arr.append(numbers[depth])
    func(depth+1)
    arr.pop()

    func(depth+1)

func(0)

print(count)