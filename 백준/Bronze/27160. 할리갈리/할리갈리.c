#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    int n;
    scanf("%d", &n);
    char fruits[5][11] = {"STRAWBERRY", "BANANA", "LIME", "PLUM"};
    int cnt[5] = {0,};

    for(int i = 0; i < n; i++){
        char temp[11];
        int num;
        scanf("%s %d", temp, &num);
        for(int j = 0; j < 4; j++){
            if (!strcmp(fruits[j], temp)){
                cnt[j] += num;
            }
        }
    }

    int f = 0;
    for(int i = 0; i < 4; i++){
        if (cnt[i] == 5){
            f = 1;
            break;
        }
    }
    if (f)
        printf("YES");
    else
        printf("NO");

    return 0;
}