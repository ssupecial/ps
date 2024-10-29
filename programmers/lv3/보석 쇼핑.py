def solution(gems):
    unique = len(set(gems))
    N = len(gems)
    answer = [1, N]

    left = 0
    right = -1
    counter = {}
    while left < N and right < N:
        if len(counter) < unique:  # 보석 부족
            right += 1
            if right == N:
                break
            counter[gems[right]] = counter.get(gems[right], 0) + 1

        else:
            if right - left < answer[1] - answer[0]:
                answer = [left + 1, right + 1]
            if counter[gems[left]] == 1:
                del counter[gems[left]]
            else:
                counter[gems[left]] -= 1
            left += 1

    return answer


answer = solution(["A", "B", "B", "B", "B", "B", "B", "C", "B", "A"])
answer = solution(["A", "AA", "AA", "AAA", "AA", "A"])
print(answer)
