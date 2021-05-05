def insertion_sort(x: list) -> list:
    for pos in range(1, len(x)):
        prev = pos - 1
        curr = pos

        while prev >= 0 and x[curr] < x[prev]:
            x[curr], x[prev] = x[prev], x[curr]

            prev = prev - 1
            curr = curr - 1
    return x