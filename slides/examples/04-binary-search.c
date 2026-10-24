#include <stdio.h>

int binary_search(const int values[], int length, int target) {
    int lo = 0;
    int hi = length;

    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        if (values[mid] == target) {
            return mid;
        }
        if (values[mid] < target) {
            lo = mid + 1;
        } else {
            hi = mid;
        }
    }

    return -1;
}

int main(void) {
    int values[] = {1, 2, 2, 5, 6};
    int length = (int)(sizeof values / sizeof values[0]);
    printf("target 5: index %d\n", binary_search(values, length, 5));
    printf("target 4: index %d\n", binary_search(values, length, 4));
    return 0;
}
