#include <stdio.h>
#include <string.h>

int main(){
  char name[11];
  int f = 0;

  for(int i = 0; i < 5; i++){
    scanf("%s", name);
    for(int j = 0; j < strlen(name)-2; j++){
      if (name[j] == 'F' && name[j+1] == 'B' && name[j+2] == 'I'){
        printf("%d ", i+1);
        f = 1;
        break;
      }
    }
  }
  if (f == 0)
    printf("HE GOT AWAY!");
  
  return 0;
}