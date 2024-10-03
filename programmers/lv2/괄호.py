from collections import deque


def check(s):
    type_a = 0
    type_b = 0
    type_c = 0

    for w in s:
        if w == "(":
            type_a += 1
        elif w == ")":
            if type_a == 0:
                return False
            else:
                type_a -= 1
        elif w == "[":
            type_b += 1
        elif w == "]":
            if type_b == 0:
                return False
            else:
                type_b -= 1
        elif w == "{":
            type_c += 1
        elif w == "}":
            if type_c == 0:
                return False
            else:
                type_c -= 1
    if (type_a + type_b + type_c) != 0:
        return False
    else:
        return True


def solution(s):
    answer = 0
    len_s = len(s)
    for i in range(len_s):
        test_s = s[i:] + s[:i]
        if check(test_s):
            # print(test_s)
            answer += 1
        print(test_s)
        print(answer)
    return answer


solution("()")
