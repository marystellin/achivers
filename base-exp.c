#include <stdio.h>

int main() {
	int b, e;
	long long result=1;
	scanf("%d",&e);
	scanf("%d",&b);
	while(e!=0)
	{
		result=result*b;
		--e;
	}
	printf("%lld",result);
	return 0;
}
