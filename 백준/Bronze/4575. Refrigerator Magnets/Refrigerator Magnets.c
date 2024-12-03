#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
  char str[61];
  int flag;
  while (1) {
    flag = 0;
    int check[27] = {
        0,
    };
    gets(str);
    if (strcmp(str, "END") == 0) {
      break;
    }
    for (int i = 0; i < strlen(str); i++) {
      if (str[i] >= 'A' && str[i] <= 'Z') {
        if (check[str[i] - 'A'] == 0) {
          check[str[i] - 'A'] = 1;
        } else if (check[str[i] - 'A'] > 0) {
          flag = 1;
          break;
        }
      }
    }
    if (flag)
      continue;
    printf("%s\n", str);
  }

  return 0;
}