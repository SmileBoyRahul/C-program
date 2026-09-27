#include<stdio.h>
int main()
{
    int password = 0;
    while (password != 1234)
    {
        printf("enter password:");
    scanf("%d", &password);
    }
    printf(" login successful");
    return 0;
}