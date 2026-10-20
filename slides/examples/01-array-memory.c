#include <inttypes.h>
#include <stdint.h>
#include <stdio.h>

int main(void) {
    int32_t values[4] = {4, 7, 2, 9};
    printf("&values     = %p\n", (void *)&values);
    printf("&values[0]  = %p\n", (void *)&values[0]);
    printf("element size = %zu bytes\n", sizeof(values[0]));
    printf("values + 1  = %p\n", (void *)(values + 1));
    printf("*(values + 1) = %" PRId32 "\n", *(values + 1));

    size_t index = 4;
    printf("Outside the array: values[%zu]\n", index);
    fflush(stdout);
    // Intentional invalid read: run with the runtime checker to see the error.
    printf("%" PRId32 "\n", values[index]);

    return 0;
}
