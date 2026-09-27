#include<stdio.h>
int main()
{
    int i;
    for(i = 1; i <= 15; i++)
    {
        if(i % 3 == 0)
        continue;
        printf("number found: %d\n", i);
    }
    return 0;
}