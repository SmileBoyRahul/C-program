#include<stdio.h>
int main()
{
    float balance = 1000;
    float amount;
    printf(" enter withdrawel amount:");
    scanf("%f\n", &amount);
    if(amount <= 1000 && amount > 0)
    {
        balance = balance - amount;
        printf(" withdrawing successful");
        printf("remaining balance : ", balance);
    }
    else
    {
        printf(" unnsufficient balance");
    }
    return 0;
}