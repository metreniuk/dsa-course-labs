def partition(values, lo, hi):
    pivot = values[lo]
    boundary = lo

    for scan in range(lo + 1, hi):
        if values[scan] < pivot:
            boundary += 1
            values[boundary], values[scan] = values[scan], values[boundary]

    values[lo], values[boundary] = values[boundary], values[lo]
    return boundary


def quick_sort(values):
    def sort_range(lo, hi):
        if hi - lo <= 1:
            return

        p = partition(values, lo, hi)
        sort_range(lo, p)
        sort_range(p + 1, hi)

    sort_range(0, len(values))


if __name__ == "__main__":
    values = [6, 2, 5, 2, 1]
    quick_sort(values)
    print(values)
