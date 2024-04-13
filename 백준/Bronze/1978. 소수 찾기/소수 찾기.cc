#include <stdio.h>
#include <math.h>

int main (){
  int n;
  int cnt = 0;
  int m[101] = {0,};
  int s[1001] = {0,};

  for(int i = 2; i < (sqrt(1000)+1); i++) {
    if(s[i] == 0) {
      for(int j = 2; j <= 1000; j++){
        if(i*j > 1000) 
          break;
        s[i*j] = 1;
      }
    }  
  }
  
  scanf("%d", &n);
  for(int i = 0; i < n; i++) {
    scanf("%d", &m[i]);
    if(m[i] == 1)
      cnt--;
    if(s[m[i]] == 0)
      cnt++;
  }
  printf("%d", cnt);
}