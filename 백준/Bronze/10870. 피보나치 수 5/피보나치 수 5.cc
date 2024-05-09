#include <stdio.h>

int main() {
    int n;
    int fibo[21] = {0,};
    fibo[1] = 1;

    for (int i = 2; i < n; i++) {
        printf("%d\n", fibo[0]);
    }

    scanf("%d", &n);
    for (int i = 2; i <= n; i++) {
        fibo[i] = fibo[i - 1] + fibo[i - 2];
    }
    printf("%d", fibo[n]);

    return 0;
}