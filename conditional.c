#include<stdio.h>
int main()
{
    int marks = 60;
    char result;
    result = ( marks >= 40)? "pass":"fail";
    printf(" result= %d", result);
    return 0;
}