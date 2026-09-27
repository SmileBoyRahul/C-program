#include<stdio.h>
int main()
{
     int age;
     printf("enter age: ");
     scanf("%d", &age);
     if(age >= 18)
     {
        if( age >= 60)
        {
            printf("eligible for vote");
            printf("senior person");
        }
        else
        {
            printf("eligible for vote");
        }
     }
     else
     {
        printf(" not eligible for vote");
     }
            if(age >= 13 )
            {
                if (age < 13)
                {
                    printf("teenager");
                }
                else
                {
                    printf(" not a teenager");
                }
            }
     return 0;
}