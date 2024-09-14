def solution(citations):
    sorted_citations = sorted(citations, reverse=True)
    for i, num in enumerate(sorted_citations):
        if num < (i + 1):
            answer = i
            return answer

    return len(sorted_citations)
