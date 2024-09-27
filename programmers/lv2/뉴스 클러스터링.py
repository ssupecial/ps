# 20:40-21:00 (20분)
def solution(str1, str2):
    dict1 = {}
    dict2 = {}

    for i in range(0, len(str1) - 1):
        tmp = str1[i : i + 2].lower()
        if tmp.isalpha():
            dict1[tmp] = dict1.get(tmp, 0) + 1

    for i in range(0, len(str2) - 1):
        tmp = str2[i : i + 2].lower()
        if tmp.isalpha():
            dict2[tmp] = dict2.get(tmp, 0) + 1

    up = 0
    down = 0
    for key in set(list(dict1.keys()) + list(dict2.keys())):
        up += min(dict1.get(key, 0), dict2.get(key, 0))
        down += max(dict1.get(key, 0), dict2.get(key, 0))

    if down == 0:
        return 1 * 65536

    answer = int(up / down * 65536)
    return answer


solution("FRANCE", "french")
