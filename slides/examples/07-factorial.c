#include <assert.h>
#include <stdio.h>

unsigned long long factorial_recursive(unsigned int n)
{
    assert(n <= 20);
    if (n == 0) {
        return 1;
    }
    return n * factorial_recursive(n - 1);
}

unsigned long long factorial_dp(unsigned int n)
{
    assert(n <= 20);
    unsigned long long fact[21];
    fact[0] = 1;
    for (unsigned int i = 1; i <= n; i++) {
        fact[i] = i * fact[i - 1];
    }
    return fact[n];
}

int main(void)
{
    printf("Recursion: %llu\n", factorial_recursive(5));
    printf("Tabulation: %llu\n", factorial_dp(5));
    return 0;
}
