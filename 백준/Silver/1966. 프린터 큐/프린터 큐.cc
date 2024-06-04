#include <stdio.h>

int Max(int arr[], int n);

int main(void) {
  int x[101];
  int n, m, a, max;
  int cnt = 0, idx = 0, odr = 0;

  scanf("%d", &n);
  for(int i = 0; i < n; i++) {
    scanf("%d %d", &m, &a);
    for(int j = 0; j < m; j++) {
      scanf("%d", &x[j]);
      cnt++;
    }
    max = Max(x, cnt);
    
    while(1) {
      if(x[idx%cnt] == max) {
        if(idx%cnt == a) {
          printf("%d\n", ++odr);
          break;
        }
        else {
          ++odr;
          x[idx%cnt] = 0;
          max = Max(x, cnt);
        }
      }
      idx++;
    }
    idx = 0;
    odr = 0;
    cnt = 0;
  }

  return 0;
}

int Max(int arr[], int n){
  int max = 0x80000000;
  for(int i = 0; i < n; i++){
    max = max < arr[i] ? arr[i] : max;
  }
  return max;
}