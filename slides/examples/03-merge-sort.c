#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>

static void sort_range(int values[], int buffer[], size_t lo, size_t hi) {
    if (hi - lo <= 1) {
        return;
    }

    size_t mid = lo + (hi - lo) / 2;
    sort_range(values, buffer, lo, mid);
    sort_range(values, buffer, mid, hi);

    size_t left = lo;
    size_t right = mid;
    for (size_t output = lo; output < hi; output++) {
        if (left < mid && (right == hi || values[left] <= values[right])) {
            buffer[output] = values[left++];
        } else {
            buffer[output] = values[right++];
        }
    }

    for (size_t output = lo; output < hi; output++) {
        values[output] = buffer[output];
    }
}

int merge_sort(int values[], size_t length) {
    if (length <= 1) {
        return 1;
    }

    int *buffer = malloc(length * sizeof *buffer);
    if (buffer == NULL) {
        return 0;
    }

    sort_range(values, buffer, 0, length);
    free(buffer);
    return 1;
}

int main(void) {
    int values[] = {6, 2, 5, 2, 1};
    size_t length = sizeof values / sizeof values[0];

    if (!merge_sort(values, length)) {
        fputs("Cannot allocate the merge buffer.\n", stderr);
        return 1;
    }

    for (size_t i = 0; i < length; i++) {
        printf("%d%s", values[i], i + 1 < length ? " " : "\n");
    }
    return 0;
}
