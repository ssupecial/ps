from itertools import combinations, product
import bisect


# a와 b 주사위의 모든 가능한 조합의 합을 비교하여 이긴 횟수를 계산하는 함수
def calculate(a_dices, b_dices):
    # a, b 각각의 주사위 목록에서 가능한 모든 값을 더한 결과를 정렬
    a_product_sum = sorted(map(sum, product(*a_dices)))
    b_product_sum = sorted(map(sum, product(*b_dices)))

    wins = 0
    num = len(a_product_sum)

    # b 합에서 하나씩 값을 뽑으면서 b 합 후보보다 큰 a 합 개수가 몇 개인지 세기
    for b in b_product_sum:
        index = bisect.bisect_left(a_product_sum, b + 1)
        wins += num - index  # b보다 큰 a 의 값 개수 누적 (== a가 이기는 횟수)

    return wins


def solution(dice):
    n = len(dice)
    a_candidates = combinations([i for i in range(n)], n // 2)

    max_wins = 0
    answer = []

    for a in a_candidates:
        b = [i for i in range(n) if i not in a]
        a_dices = [dice[i] for i in a]  # a에 해당하는 주사위 리스트
        b_dices = [dice[i] for i in b]  # b에 해당하는 주사위 리스트
        wins = calculate(a_dices, b_dices)
        if wins > max_wins:
            max_wins = wins
            answer = list(a)

    answer = [x + 1 for x in answer]
    return answer


answer = solution(
    [[1, 2, 3, 4, 5, 6], [3, 3, 3, 3, 4, 4], [1, 3, 3, 4, 4, 4], [1, 1, 4, 4, 5, 5]]
)
print(answer)
# solution([[1, 2, 3, 4, 5, 6], [2, 2, 4, 4, 6, 6]])
# solution(
#     [
#         [40, 41, 42, 43, 44, 45],
#         [43, 43, 42, 42, 41, 41],
#         [1, 1, 80, 80, 80, 80],
#         [70, 70, 1, 1, 70, 70],
#     ]
# )
