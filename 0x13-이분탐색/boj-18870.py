n = int(input())
arr = list(map(int, input().split()))

sorted_arr = sorted(list(set(arr)))

def find_half(start_idx, finish_idx, value):
    if start_idx == finish_idx:
        return start_idx
    half_idx = (start_idx+finish_idx)//2
    half_value = sorted_arr[half_idx]
    if value == half_value:
        return half_idx
    elif value < half_value:
        return find_half(start_idx, half_idx, value)
    else:
        return find_half(half_idx+1, finish_idx, value)

len_n = len(sorted_arr)-1
result = [find_half(0, len_n, value) for value in arr]
print(" ".join(list(map(str, result))))