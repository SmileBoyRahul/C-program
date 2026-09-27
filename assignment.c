#include <stdio.h>
int main()
{
    int fee = 1000;
    printf("fee: %d\n", fee);
    fee+=500;
    printf("after fee+=500:%d\n", fee);
    fee-=300;
    printf("after fee-=300:%d\n", fee);
    fee*=2;
    printf("after fee*=2:%d\n", fee);
    fee/=2;
    printf("after fee/=2:%d\n", fee);
    return 0; 
}