#include <stdio.h>
 
int main() {
	long  long n;
	int count=0;
	scanf("%d",&n);
	while(n!=0)
	{
		n/=10;
		++count;
	}
	printf("%d",count);
	return 0;
}
