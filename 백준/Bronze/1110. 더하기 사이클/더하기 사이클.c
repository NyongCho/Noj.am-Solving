#include <stdio.h>

int main() {
  int n,m,u,c=0;
  scanf("%d",&n);
  int f=n;
  while(n!=u || c == 0){
    u=f%10*10;
    m=f/10+f%10;
    u+=m%10;
    c++;
    f=u;
  }
  printf("%d",c);
  
  return 0;
}