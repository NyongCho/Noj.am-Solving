#include <iostream>
using namespace std;

int main(){
  int n, answer = 0, key = 666, i = 665;
  scanf("%d", &n);
  while(n){
    i++;
    int x = i;
    while(x >= 666){
      int temp = x%1000;
      if(temp/666.0 == 1.0){
        answer = i;
        n--;
        break;
      }
      x /= 10;
    }
  }
  printf("%d", answer);

  return 0;
}