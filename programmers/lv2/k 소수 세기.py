def is_prime(n):
    if n == 1:
        return False

    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1

    return True


def solution(n, k):
    result = ""
    while n >= 1:
        result = str(n % k) + result
        n = n // k

    arr = [int(num) for num in result.split("0") if num != ""]

    answer = sum(list(map(is_prime, arr)))
    return answer


answer = solution(437674, 3)
print(answer)

answer = solution(110011, 10)
print(answer)

answer = solution(797161, 3)
print(answer)

answer = solution(10, 10)
print(answer)
