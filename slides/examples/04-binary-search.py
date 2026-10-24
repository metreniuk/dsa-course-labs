def binary_search(values, target):
    lo, hi = 0, len(values)

    while lo < hi:
        mid = lo + (hi - lo) // 2
        if values[mid] == target:
            return mid
        if values[mid] < target:
            lo = mid + 1
        else:
            hi = mid

    return -1


if __name__ == "__main__":
    values = [1, 2, 2, 5, 6]
    for target in (5, 4):
        print(f"target {target}: index {binary_search(values, target)}")
