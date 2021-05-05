def bubble_sort(x: list) -> list:
    for _ in range(1, len(x)):
        for pos in range(1, len(x)):
            curr = pos
            prev = pos - 1
            if x[prev] > x[curr]:
                x[prev], x[curr] = x[curr], x[prev]
    return x