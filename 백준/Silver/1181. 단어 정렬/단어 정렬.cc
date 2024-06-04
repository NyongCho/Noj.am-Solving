#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

bool cmp(string a, string b) {
	if (a.length() != b.length())
		return a.length() < b.length();
	else
		return a < b;
}

int main() {
	int n;
	scanf("%d", &n);
	vector<string> s(n);

	for (int i = 0; i < n; i++) {
		cin >> s[i];
	}
	sort(s.begin(), s.end(), cmp);
	for (int i = 0; i < n; i++) {
		for (int j = i + 1; j < n; j++) {
			if (s[i] == s[j]) {
				s.erase(s.begin()+j);
				n--;
				j--;
			}

		}
	}
	for (int i = 0; i < n; i++) {
		cout << s[i] << "\n";
	}

	return 0;
}