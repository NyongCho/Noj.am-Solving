#include <stdio.h>
#include <stdlib.h>

int main() {
  int n;
  scanf("%d", &n);
  int *arr = (int *)malloc(sizeof(int) * (n+1));
  int tmp;

  for (int i = 0; i < n; i++) {
    scanf("%d", &tmp);
    int start = i - tmp;
    for (int j = i + 1; j >= start; j--) {
      *(arr + j) = *(arr + j - 1);
    }
    *(arr + start) = i + 1;
  }

  for (int i = 0; i < n; i++) {
    printf("%d ", *(arr + i));
  }

  return 0;
}