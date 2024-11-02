# https://school.programmers.co.kr/learn/courses/30/lessons/17687?language=python3
def convert_n(x, base):
    if x == 0:
        return "0"

    """Claude를 통해 개선한 코드"""
    digits = "0123456789ABCDEF"
    result = ""

    while x >= 1:
        result = digits[x % base] + result
        x = x // base

    """기존에 작성한 코드"""
    # tmp = ""
    # while x >= 1:
    #     rest = x % n
    #     rest = f"{rest}" if rest < 10 else chr(ord("A") + (rest - 10))
    #     tmp = rest + tmp
    #     x = x // n

    return result


def solution(n, t, m, p):
    all = ""
    i = 0
    while len(all) < t * m:
        all += convert_n(i, n)
        i += 1

    answer = all[p - 1 : t * m : m]

    # answer = "".join([all[p - 1 + i * m] for i in range(t)])
    return answer


# solution(2, 4, 2, 1)
solution(16, 16, 2, 1)
