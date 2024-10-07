#include <iostream>
#include <string.h>
#include <algorithm>

int main() {
	char s[2890] = { 0, };
	int a, b;
	int c = 0, f = 0;
	int n = 1, x;

	scanf("%s", s);
	
	while (n < 4) {
		for (int i = 0; i < n; i++) {
			c *= 10;
			c += s[i] - 48;
		}
		a = c;
		for (int i = 0; i < strlen(s);) {
			x = i;
			if (c < 10) {
				i += 1;
				if (c != s[x] - 48) {
					f = 1;
					break;
				}
			}
			else if (c >= 10 && c < 100) {
				i += 2;
				if (c != (s[x] - 48) * 10 + s[x + 1] - 48) {
					f = 1;
					break;
				}
			}
			else if (c >= 100) {
				i += 3;
				if (c != (s[x] - 48) * 100 + (s[x + 1] - 48) * 10 + s[x + 2] - 48) {
					f = 1;
					break;
				}
			}
			c++;
		}
		if (f == 0) {
			b = c - 1;
			break;
		}
		c = 0;
		n++;
		f = 0;
	}

	printf("%d %d", a, b);

	return 0;
}