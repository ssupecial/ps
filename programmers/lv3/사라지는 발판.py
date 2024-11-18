#  22:10~23:30
def calculate(a: str, op: str, b: str, digit: int) -> str:
    max_len = max(len(a), len(b))
    a = list(map(int, a[::-1]))
    b = list(map(int, b[::-1]))

    # 두 숫자의 길이를 max_len으로 맞추기
    a += [0] * (max_len - len(a))
    b += [0] * (max_len - len(b))

    result = []
    tmp = 0
    if op == "+":
        for _a, _b in zip(a, b):
            num = _a + _b + tmp
            if num >= digit:
                tmp = 1
                num = num - digit
            else:
                tmp = 0
            result.append(num)
        if tmp == 1:
            result.append(1)
    else:
        for _a, _b in zip(a, b):
            num = _a - _b - tmp
            if num < 0:
                tmp = 1
                num = num + digit
            else:
                tmp = 0
            result.append(num)

    result = "".join(map(str, result[::-1])).lstrip("0")
    return result if result else "0"


def solution(expressions):
    answer = []

    know = []
    have_to_know = []
    candidates = None
    numbers = []
    for expression in expressions:
        a, op, b, _, c = expression.split(" ")
        numbers += (a + b + c) if c != "X" else (a + b)
        if c == "X":
            have_to_know.append([a, op, b])
        else:
            know.append([a, op, b, c])

    max_digit = max(int(d) for d in numbers if d.isdigit())
    candidates = [i for i in range(max(2, max_digit + 1), 10)]

    extract = set()
    for a, op, b, c in know:
        for candidate in candidates:
            if c != calculate(a, op, b, candidate):
                extract.add(candidate)

    candidates = list(set(candidates) - extract)

    # 후보 진수들로 결과 계산
    for a, op, b in have_to_know:
        tmp = []
        for candidate in candidates:
            tmp.append(calculate(a, op, b, candidate))
        tmp_set = set(tmp)
        if len(tmp_set) == 1:
            answer.append(f"{a} {op} {b} = {tmp[0]}")
        else:
            answer.append(f"{a} {op} {b} = ?")

    return answer


solution(["14 + 3 = 17", "13 - 6 = X", "51 - 5 = 44"])
