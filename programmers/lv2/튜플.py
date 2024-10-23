def solution(s):
    answer = []

    tmp_arr = []
    tmp_int = ""
    results = []

    for w in s:
        if w == "{":
            continue
        elif w == "}":
            if tmp_int != "":
                tmp_arr.append(int(tmp_int))
            results.append(tmp_arr)
            tmp_arr = []
            tmp_int = ""
        elif w == ",":
            if tmp_int != "":
                tmp_arr.append(int(tmp_int))
                tmp_int = ""
        else:
            tmp_int += w

    results.sort(key=len)
    for result in results:
        for value in result:
            if value not in answer:
                answer.append(value)
    return answer


# answer = solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")
answer = solution("{{123}}")
print(answer)
