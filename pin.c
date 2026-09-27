#include<stdio.h>
int main()
{
    int pin;
    do
    {
       printf("enter the pin: ");
       scanf("%d", &pin);
    } 
    while (pin != 1234);
    printf("correct pin");
    return 0;
    
}