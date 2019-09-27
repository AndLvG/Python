arr = [1]


def catalan(n):
    global arr
    while len(arr) != n + 1:
        arr.append(int(int(arr[len(arr) - 1]) * (4 * len(arr) - 2) // (len(arr) + 1)))
    return arr[n]




print(catalan(0))


