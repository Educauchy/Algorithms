def selection_sort(x: list) -> list:
    for j in range(1, len(x)):
        key = x[j]
        i = j - 1
        while i >= 0 and x[i] > key:
            x[i + 1], x[i] = x[i], x[i + 1]
            i = i - 1
        x[i + 1] = key
    return x