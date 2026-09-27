#include<stdio.h>
int main()
{
    char choice;
    do
    {
    printf("welcome to the program:");
    printf(" \n do you want to continue = y/n");
    scanf("%c", &choice);
    } 
    while (choice == 'y' || choice == 'n');
    printf("program ended");
    return 0;
    
}