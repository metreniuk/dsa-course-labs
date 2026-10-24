#include <stddef.h>
#include <stdio.h>

static void swap(int *left, int *right) {
    int saved = *left;
    *left = *right;
    *right = saved;
}

static size_t partition(int values[], size_t lo, size_t hi) {
    int pivot = values[lo];
    size_t boundary = lo;

    for (size_t scan = lo + 1; scan < hi; scan++) {
        if (values[scan] < pivot) {
            boundary++;
            swap(&values[boundary], &values[scan]);
        }
    }

    swap(&values[lo], &values[boundary]);
    return boundary;
}

static void sort_range(int values[], size_t lo, size_t hi) {
    if (hi - lo <= 1) {
        return;
    }

    size_t p = partition(values, lo, hi);
    sort_range(values, lo, p);
    sort_range(values, p + 1, hi);
}

void quick_sort(int values[], size_t length) {
    sort_range(values, 0, length);
}

int main(void) {
    int values[] = {6, 2, 5, 2, 1};
    size_t length = sizeof values / sizeof values[0];
    quick_sort(values, length);
    for (size_t i = 0; i < length; i++) {
        printf("%d%s", values[i], i + 1 < length ? " " : "\n");
    }
    return 0;
}
