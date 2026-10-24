def merge_sort(values):
    buffer = [0] * len(values)

    def sort_range(lo, hi):
        if hi - lo <= 1:
            return

        mid = lo + (hi - lo) // 2
        sort_range(lo, mid)
        sort_range(mid, hi)

        left, right = lo, mid
        for output in range(lo, hi):
            if left < mid and (right == hi or values[left] <= values[right]):
                buffer[output] = values[left]
                left += 1
            else:
                buffer[output] = values[right]
                right += 1

        for output in range(lo, hi):
            values[output] = buffer[output]

    sort_range(0, len(values))


if __name__ == "__main__":
    values = [6, 2, 5, 2, 1]
    merge_sort(values)
    print(values)
