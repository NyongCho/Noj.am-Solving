#include <stdio.h>

int main() {
    int N;
    int X, S;
    int is_available = 0;
    scanf("%d", &N);
    scanf("%d %d", &X, &S);
    for(int i = 0; i < N; i++){
        int price, attack;
        scanf("%d %d", &price, &attack);
        if(X < price)
            continue;
        if(attack > S)
            is_available = 1;
    }
    if(is_available)
        printf("YES");
    else
        printf("NO");

    return 0;
}