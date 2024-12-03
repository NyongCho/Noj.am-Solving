#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int stack[100001];
int n, top = -1, tmp;

int main() {
  scanf("%d", &n);

  for (int i = 0; i < n; i++) {
    scanf("%d", &tmp);
    if (top == -1) {
      stack[++top] = tmp;
      continue;
    }

    while (top != -1 && stack[top] <= tmp) {
      top--;
    }
    stack[++top] = tmp;
  }
  printf("%d", top+1);

  return 0;
}