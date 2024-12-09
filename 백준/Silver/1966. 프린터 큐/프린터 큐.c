#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int max_check(int *arr, int idx, int n){
    int max = 0;
    for(int i = 0; i < n; i++){
        if (max < arr[i]){
            max = arr[i];
        }
    }
    if (max != arr[idx])
        return 0;
    else
        return 1;
}

int main() {
    int t;
    scanf("%d", &t);
    while(t--){
        int n, m;
        scanf("%d %d", &n, &m);
        int queue[101] = {0,};

        for(int i = 0; i < n; i++){
            scanf("%d", &queue[i]);
        }

        int cnt = 0;
        for(int i = 0; queue[m] != 0; i = (i+1)%n){
            if (queue[i] == 0)
                continue;
            if (max_check(queue, i, n)) {
                // printf("q[%d] = %d\n", i, queue[i]);
                queue[i] = 0;
                cnt ++;
            }
        }
        printf("%d\n", cnt);
    }
    
    return 0;
}