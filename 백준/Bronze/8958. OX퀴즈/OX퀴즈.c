#include <stdio.h>
#include <string.h>

int n, sum, cnt;
char arr[81];

int main () {
	scanf("%d", &n);
	for(int i = 0; i < n; ++i) {
		scanf("%s", arr);
		for (int j = 0; j <strlen(arr); ++j) {
			if (arr[j] == 'O') cnt++;
			else if (arr[j] == 'X' && arr[j-1] == 'O'){
				for (int k = 1; k <= cnt; ++k) {
					sum += k;
				}
				cnt = 0;
			}
		}
		for (int k = 1; k <= cnt; ++k) {
			sum += k;
		}
		printf("%d\n",sum);
		sum = 0;
		cnt = 0;
	}

	/*for (int i = 0; i < n; ++i) {
		printf("%d\n", ct[i]);
	}*/
	return 0;
}