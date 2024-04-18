/* 이진수 덧셈 */
// #include <stdio.h>

// int main() {
//     int n, m;
//     scanf("%d %d", &n, &m);
//     int s = n+m;

//     if (s == 0) {
//         printf("0");
//         return 0;
//     }
//     int cnt = 0;
//     int len = 0;
//     int r = 0;

//     while (s != 0){
//         int o = s%10;
//         if (o > 1) {
//             s += 10;
//             o -= 2;
//         }
//         if (o == 0 && len == cnt){
//             cnt++;
//         }
//         r = r*10 +o;
//         s /= 10;

//         len++;
//     }

//     while (r != 0){
//         printf("%d", r%10);
//         r /=10;
//     }
    
//     for (int i = 0; i < cnt; i++){
//         printf("0");
//     }

//     return 0;
// }

#include <stdio.h>

int main(void)
{
	int m, n, det;
	int s=0, min=10001;

	scanf("%d %d", &m, &n);

	if (m == 1)
        m = 2;

	for (int i = m; i <= n; i++)
	{
		int f = 0;
		for (int j = 2; j*j <= i; j++)
		{
			if(i%j == 0)
                f = 1;
		}
		if (!f)
		{
			s = s+i;
			if(min>i)
                min=i;
		}
	}
	if(s == 0)
        printf("-1");
	else
        printf("%d\n%d", s, min);
        
	return 0;
}
