#pragma warning (disable:4996)
#include <stdio.h>

//2839번 설탕 배달
int main() {
	int N, i;

	scanf("%d", &N);

	int arr[5000] = { 0 };

	for (i = 1; i <= N; i++) {
		arr[i] = -1;
	}

	for (i = 3; i <= N; i++) {
		if (arr[i - 3] != -1) {
			arr[i] = arr[i - 3] + 1;
		}
		if (i - 5 >= 0 && arr[i - 5] != -1) {
			if ((arr[i] > arr[i - 5] + 1 && arr[i - 5] > 0) || (arr[i] < 0))
				arr[i] = arr[i - 5] + 1;
		}
	}
	//for (i = 1; i <= N; i++) {
	//	printf("%d %d\n", i, arr[i]);
	//}

	printf("%d", arr[N]);
}