from collections import deque


def check(deck1, deck2, value):
    for card in deck1:
        if (value - card) in deck2:
            deck1.remove(card)
            deck2.remove(value - card)
            return True

    return False


def solution(coin, cards):
    len_n = len(cards)
    initial = cards[: len_n // 3]
    rest = deque(cards[len_n // 3 :])
    hand = []
    turn = 1
    print(initial, hand)

    while rest and coin >= 0:
        hand.append(rest.popleft())
        hand.append(rest.popleft())

        if check(initial, initial, len_n + 1):
            pass
        elif coin >= 1 and check(initial, hand, len_n + 1):
            coin -= 1
        elif coin >= 2 and check(hand, hand, len_n + 1):
            coin -= 2
        else:
            break

        turn += 1

    return turn


answer = solution(10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])
print(answer)
