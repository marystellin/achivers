#include <stdio.h>

int main() {
	int i,n,m;
	scanf("%d",&n);
	scanf("%d",&m);
	for(i=n;i<=m;i++)
	{
		if(i%2==1)
		{
			printf("%d",i);
		}
	}
	return 0;
}
