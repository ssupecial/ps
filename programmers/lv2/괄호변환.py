# 괄호 변환
# https://school.programmers.co.kr/learn/courses/30/lessons/60058


def check(input):  # 올바른 괄호 문자열인지 확인
    arr = []
    for w in input:
        if w == "(":
            arr.append(w)
        elif w == ")":
            if arr == []:
                return False
            else:
                arr.pop()

    if arr == []:
        return True
    else:
        return False


def separate(input):  # 균형잡힌 괄호 문자열 나누기
    num = 0
    index = 1
    if input[0] == "(":
        num += 1
    else:
        num -= 1
    for w in input[1:]:
        if num == 0:
            break
        if w == "(":
            num += 1
        elif w == ")":
            num -= 1
        index += 1
    u = input[:index]
    v = input[index:]
    return u, v


def opposite(input):  # 괄호 뒤집기
    result = ""
    for w in input:
        if w == "(":
            result += ")"
        else:
            result += "("
    return result


def func(input):  # 재귀
    if input == "":
        return ""
    if check(input):
        return input

    u, v = separate(input)
    if check(u):
        return u + func(v)
    else:
        return "(" + func(v) + ")" + opposite(u[1:-1])


def solution(p):
    answer = func(p)
    return answer
