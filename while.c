#include<stdio.h>
int main()
{
    int roll;
    printf("enter positive roll number:");
    scanf("%d", &roll);
    while(roll <= 0)
    {
        printf("invalid roll");
        printf("enter again");
        scanf("%d", &roll);

    }
    return 0;
}