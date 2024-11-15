# 22:00-22:10
def solution(cards):
    cards = [0] + cards
    visited = [False] * len(cards)

    cycles = []

    for i in range(1, len(cards)):
        if not visited[i]:
            cycle = []
            cur = i
            while not visited[cur]:
                cycle.append(cur)
                visited[cur] = True
                cur = cards[cur]

            cycles.append(len(cycle))

    answer = 0
    if len(cycles) >= 2:
        cycles.sort(reverse=True)
        answer = cycles[0] * cycles[1]
    return answer


solution([8, 6, 3, 7, 2, 5, 1, 4])
