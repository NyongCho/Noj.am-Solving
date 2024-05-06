#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);

    int x = 0, y = 0, limit = 1, count = 0, d = 0;

    for (int i = 1; i <= n; i++) {
        if (d == 0) y++; // 위
        else if (d == 1) x++; // 오른쪽
        else if (d == 2) y--; // 아래
        else if (d == 3) x--; // 왼쪽

        count = count + 1;
        if (count == limit) {
            count = 0;
            d = (d + 1) % 4;  // 90도 회전

            if (d == 0 || d == 2) {  // 오른쪽 또는 왼쪽으로 방향 전환
                limit++;
            }
        }
    }

    printf("%d %d", x, y);

    return 0;
}