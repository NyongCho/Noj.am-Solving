//#include <stdio.h>
//#define MACHINE 500001
//#define N 1000001
//
//int up[MACHINE];
//int down[MACHINE];
//int temp[MACHINE];
//int tree[N];
//int hash[N];
//
//int sum(int *tree, int i) {
//	int ret = 0;
//	while (i > 0) {
//		ret += tree[i];
//		i -= (i & -i);
//	}
//	return ret;
//}
//
//void update(int *tree, int i, const int num, const unsigned int size) {
//	while (i <= size) {
//		tree[i] += num;
//		i += (i & -i);
//	}
//}
//
//int main() {
//	int i, n;
//	long long int ret = 0;
//
//	scanf("%d", &n);
//
//	for (i = 1; i <= n; ++i) {
//		scanf("%d", &up[i]);
//		hash[up[i]] = i;
//	}
//	for (i = 1; i <= n; ++i) {
//		scanf("%d", &down[i]);
//		update(tree, hash[down[i]], 1, n);
//		ret += sum(tree, n) - sum(tree, hash[down[i]]);
//	}
//	printf("%lld", ret);
//}
#include <iostream>
#include <algorithm>
#include <queue>
using namespace std;

int main() {
	int bf[31][31] = { 0, };
	int af[31][31] = { 0, }; 
	int n, m;
	int c, g;
	int f = 0;

	queue <pair<int, int>> d;
	queue <pair<int, int>> a;
	
	scanf("%d %d", &n, &m);
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			scanf("%d", &bf[i][j]);
		}
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			scanf("%d", &af[i][j]);
			if (af[i][j] != bf[i][j]) {
				d.push({ i, j });
				f += 1;
			}
		}
	}
	if (f == 0) {
		printf("YES");
	}
	else {
		f = 0;
		a.push(d.front());
		d.pop();
		int x = a.front().first;
		int y = a.front().second;
		g = af[x][y];
		c = bf[x][y];
		a.push({ x + 1,y });
		a.push({ x, y + 1 });
		a.push({ x - 1,y });
		a.push({ x, y - 1 });

		while (!a.empty()) {
			x = a.front().first;
			y = a.front().second;
			if (bf[x][y] == c) {
				bf[x][y] = g;
				a.push({ x + 1,y });
				a.push({ x, y + 1 });
				a.push({ x - 1,y });
				a.push({ x, y - 1 });
			}
			a.pop();
		}
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (af[i][j] != bf[i][j]) {
					f += 1;
				}
			}
		}
		if (f == 0)
			printf("YES");
		else
			printf("NO");
	}

	return 0;
}