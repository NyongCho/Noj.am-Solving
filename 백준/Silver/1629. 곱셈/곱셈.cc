#include <iostream>
#include <algorithm>
using namespace std;
typedef long long ll;

ll power(int a, int b, int c) {
	if (b == 0)
		return 1;

  ll res = power(a, b / 2, c);
  ll t = res * res % c;
  
	if (b % 2 == 0)
		return t;
	else
		return a * t % c;
}

int main() {
	int a,n,r;
  cin >> a >> n >> r;
  printf("%lld", power(a,n,r));

	return 0;
}