#include<stdio.h>
int main()
{
    int marks = 97;
    if( marks >= 90)
    {
        printf(" grade A ");
    }
    else if( marks < 90 && marks >= 80)
    {
        printf(" Grade B");
    }
    else if( marks < 80 && marks >= 70)
    {
        printf(" Grade C");
    }
    else 
    {
        printf(" Grade D");
    }
    return 0;
}