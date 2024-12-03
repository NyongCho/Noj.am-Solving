#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
  int n;
  char temp[26];

  scanf("%d", &n);
  getchar();
  for (int i = 0; i < n; i++) {
    gets(temp);
    int len = strlen(temp);
    int n_word = 0, s = 0;
    char **words = NULL;

    for (int j = 0; j <= len; j++) {
      if (temp[j] == ' ' || temp[j] == '\0') {
        n_word++;
        words = (char **)realloc(words, sizeof(char *) * (n_word));
        words[n_word - 1] = (char *)malloc(sizeof(char) * (j - s));
        temp[j] = '\0';
        strcpy(words[n_word - 1], temp + s);
        s = j + 1;
      }
    }

    printf("Case #%d: ", i + 1);
    for (int j = 0; j < n_word - 1; j++) {
      printf("%s ", words[n_word - j - 1]);
    }
    printf("%s\n", words[0]);

    for (int j = 0; j < n_word; j++) {
      free(words[j]);
    }
    free(words);
  }

  return 0;
}