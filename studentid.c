#include <stdio.h>
int main()
{
    int i, searchid=25;
    for (i = 1; i <= 100; i++)
    {
        if (searchid == 25)
        break;
        printf("%d\n", i);
    }
    return 0;
}