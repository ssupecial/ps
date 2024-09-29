n = int(input())
arr_n = sorted(list(map(int, input().split())))
m = int(input())
arr_m = list(map(int, input().split()))

def find_half(start_idx, finish_idx, value):
    if start_idx == finish_idx:
        if value == arr_n[start_idx]:
            return True
        return False
    half_idx = (start_idx+finish_idx)//2
    half_value = arr_n[half_idx]
    if value == half_value:
        return True 
    elif value < half_value:
        return find_half(start_idx, half_idx, value)
    else:
        return find_half(half_idx+1, finish_idx, value)

len_n = len(arr_n) -1
for value in arr_m:
    if find_half(0, len_n, value):
        print(1)
    else:
        print(0)