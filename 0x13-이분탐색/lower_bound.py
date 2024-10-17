# key 이상의 값이 처음 나오는 위치를 찾아보자!
# 핵심 : 같거나 작은 배열들을 계속 구해나가면서 마지막에 해당 배열의 가장 오른쪽 인덱스를 넘겨주면 된다
def lower_bound(arr, target):
    l = 0
    r = len(arr) - 1
    while l < r:  # 같으면 종료되어야함! (기본 이분탐색처럼 같으면 안됨)
        mid = (l + r) // 2
        if arr[mid] < target:
            l = mid + 1
        elif arr[mid] == target:
            r = mid
        elif arr[mid] > target:
            r = mid

    return r


# key 초과의 값이 처음 나오는 위치를 찾아보자!
# 핵심: 해당 키보다 큰 배열을 계속 구해가면서 마지막에 해당 배열의 가장 오른쪽 인덱스를 넘겨주면 된다
def upper_bound(arr, target):
    l = 0
    r = len(arr) - 1
    while l < r:
        mid = (l + r) // 2
        if arr[mid] == target:
            l = mid + 1
        elif arr[mid] < target:
            l = mid + 1
        elif arr[mid] > target:
            r = mid

    return r
