def cost(name_index, price, parent, results):
    if name_index == 0:
        return

    next_revenue = int(price * 0.1)
    if next_revenue < 1:
        revenue = price
        results[name_index] += revenue
        return

    revenue = price - next_revenue
    results[name_index] += revenue
    cost(parent[name_index], next_revenue, parent, results)


def solution(enroll, referral, seller, amount):
    parent = [0] * (len(enroll) + 1)
    name_to_index = {}
    name_to_index["-"] = 0
    for i, (name, referral_name) in enumerate(zip(enroll, referral)):
        name_to_index[name] = i + 1
        parent[i + 1] = name_to_index[referral_name]

    results = [0] * (len(enroll) + 1)
    for name, num in zip(seller, amount):
        cost(name_to_index[name], 100 * num, parent, results)

    return results[1:]


# solution(
#     ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
#     ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
#     ["young", "john", "tod", "emily", "mary"],
#     [12, 4, 2, 5, 10],
# )

solution(
    ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
    ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
    ["sam", "emily", "jaimie", "edward"],
    [2, 3, 5, 4],
)
