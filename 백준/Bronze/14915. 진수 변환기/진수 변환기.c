
#include <stdio.h>

int main(void) {
  int m, n;
  scanf("%d %d", &m, &n);

  int x = n;
  while (m >= x) {
    x *= n;
  }
  x /= n;

  while (x > 0) {
    int a = m / x;
    if (a > 9) {
      printf("%c", a + 55);
    }
    else
      printf("%d", a);
    m %= x;
    x /= n;
  }

  return 0;
}
