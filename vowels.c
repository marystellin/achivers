#include <stdio.h>

int main()
{
	char r;
	scanf("%s",&r);
	if(r=='a'||r=='e'||r=='i'||r=='o'||r=='u')
	{
		printf("vowels");
	}
	else if(r>="a"&&r<="z")
	{
		printf("consodent");
	}
	else
	{
		printf("invalid");
	}
	
	return 0;
}
