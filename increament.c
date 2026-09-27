#include<stdio.h>
int main()
{
    int attandance = 10;
    int a;
    a = ++attandance;
    printf("pre inncreament : a = %d, attandance = %d\n", a, attandance);
    attandance = 10;
    a = attandance++;
    printf("post increament : a = %d, attandance = %d\n", a, attandance);
    return 0;
}