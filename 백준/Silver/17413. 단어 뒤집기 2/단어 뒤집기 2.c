#include <stdio.h>
#include <string.h>

int main() {
  char str[100001];
  int tmp_len = 0;
  int pre_idx = 0;
  int f = 0;

  gets(str);
  int len = strlen(str);

  for (int i = 0; i < len; i++) {
    if (str[i] == '<') {
      f = 1;
      for (int j = 0; j < tmp_len; j++) {
        printf("%c", *(str + pre_idx + tmp_len - j - 1));
      }
      pre_idx  = i + 1;    
      tmp_len = 0;
      printf("%c", str[i]);
    }
    else if (str[i] == '>') {
      f = 0;
      for (int j = 0; j < tmp_len; j++) {
        printf("%c", *(str + pre_idx + j));
      }
      pre_idx = i + 1;
      tmp_len = 0;
      printf("%c", str[i]);
    }
    else if (str[i] == ' ' && f == 0) {
      for (int j = 0; j < tmp_len; j++) {
        printf("%c", *(str + pre_idx + tmp_len - j - 1));
      }
      pre_idx = i + 1;
      tmp_len = 0;
      printf("%c", str[i]);
    } else
      tmp_len++;
  }
  for (int j = 0; j < tmp_len; j++) {
    printf("%c", *(str + pre_idx + tmp_len - j - 1));
  }

  return 0;
}