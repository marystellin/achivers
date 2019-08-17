#include <stdio.h>

int main() {
	int n, remainder, reverse=0, temp;
	scanf("%d",&n);
	temp=n;
	while(temp!=0)
	{
		remainder=n%10;
		reverse=reverse*10+remainder;
		n=n/10;
	}
	if(reverse==temp)
	{
		printf("yes");
	}
	else
	{
		printf("not");
	}
	return 0;
}
