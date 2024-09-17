# 양궁대회
# https://school.programmers.co.kr/learn/courses/30/lessons/92342


def solution(n, info):
    answer = [-1]
    max_game_count = 0

    for tmp in range(3**11):
        result = []
        count = 0
        game_count = 0
        i = tmp

        for j in range(11):  # 10-j 점수 가져갈지 말지
            cur = i % 3
            i = i // 3

            if cur == 0:  # 이기기
                need_num = info[j] + 1
                game_count += 10 - j
            elif cur == 1:  # 비기기
                need_num = info[j]
                if info[j] > 0:
                    game_count -= 10 - j
            elif cur == 2:  # 지기
                need_num = 0
                if info[j] > 0:
                    game_count -= 10 - j

            result.append(need_num)
            count += need_num
            if count > n:
                break

        if count <= n and game_count > 0:  # 11개 다 채우고 난 후
            result[-1] += n - count
            if game_count > max_game_count:
                max_game_count = game_count
                answer = result[:]
            if game_count == max_game_count:
                for k in range(10, -1, -1):
                    if result[k] > answer[k]:
                        answer = result[:]
                        break
                    elif answer[k] > result[k]:
                        break

    return answer


output = solution(1, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
# output = solution(9, [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1])

print(output)
