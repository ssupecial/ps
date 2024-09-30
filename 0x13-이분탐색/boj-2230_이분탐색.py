n, m = list(map(int, input().split()))
numbers = []
for i in range(n):
    numbers.append(int(input()))

numbers.sort()
answers = None

def find_half(start_idx, finish_idx, value):
    if start_idx == finish_idx:
        if numbers[start_idx] < value:
            return -1
        return numbers[start_idx]

    half_idx = (start_idx + finish_idx) // 2
    half_value = numbers[half_idx]

    if value == half_value:
        return half_value
    elif value < half_value:
        return find_half(start_idx, half_idx, value)
    else:
        return find_half(half_idx+1, finish_idx, value)
    

len_n = len(numbers)-1
for i, num in enumerate(numbers):

    result = find_half(i, len_n, m+num)
    if result != -1:
        if answers is None:
            answers = result-num
        else:
            answers = min(answers, result-num)

    

print(answers)