discounts = []
results = []


def calculate(discount_threshold, plus_threshold, emoticons):
    price = 0
    for i, emoticon in enumerate(emoticons):
        if discounts[i] >= discount_threshold:
            price += int(emoticon * (100 - discounts[i]) * 0.01)
    if price >= plus_threshold:
        return 1, 0
    else:
        return 0, price


def count_people_and_overall(users, emoticons):
    global discounts, results
    plus = 0
    overall = 0
    for discount_threshold, plus_threshold in users:
        is_plus, price = calculate(discount_threshold, plus_threshold, emoticons)
        plus += is_plus
        overall += price

    results.append([plus, overall])


def solution(users, emoticons):
    global results
    len_emoticons = len(emoticons)

    def func(depth):
        if depth == len_emoticons:
            count_people_and_overall(users, emoticons)
            return

        for i in range(10, 41, 10):
            discounts.append(i)
            func(depth + 1)
            discounts.pop()

    func(0)
    results.sort(key=lambda x: (x[0], x[1]), reverse=True)
    return results[0]
