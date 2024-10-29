def convert_two(n):
    arr = ""
    while n >= 1:
        arr = str(n % 2) + arr
        n = n // 2

    return arr


def tree(arr):
    if len(arr) == 1:
        return True

    if "1" not in arr:
        return True

    if "0" not in arr:
        return True

    root = len(arr) // 2

    if arr[root] == "0":
        return False

    # 왼쪽
    left = tree(arr[:root])

    # 오른쪽
    right = tree(arr[root + 1 :])

    return left and right


def solution(numbers):
    answer = []
    for number in numbers:
        arr = convert_two(number)
        length = len(arr)

        i = 0
        while True:
            start = 2**i - 1
            end = 2 ** (i + 1) - 1

            if length > start and length <= end:
                diff = end - length
                arr = "0" * diff + arr
                break

            i += 1

        result = 1 if tree(arr) else 0
        answer.append(result)

    return answer


answer = solution([128])
# answer = solution([128])
print(answer)
