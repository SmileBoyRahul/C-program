#include<stdio.h>
int main()
{
    int unit;
    float bill;
    printf(" enter unit");
    scanf("%d", &unit);
    if(unit >= 200)
    {
        bill = unit * 8;
        printf("electricity bill: ", bill);
    }
    else if(unit < 200 && unit >= 100)
    {
        bill = unit * 5;
        printf("electricity bill: ", bill);
    }
    else if(unit < 100 && unit > 0)
    {
        bill = unit * 3;
        printf("electricity bill: ", bill);
    }
    else 
    {
        printf("invalid unit");
    }
    return 0;
}