
/*
Author;  Captain Murlidhar Singh
purpose; Multiplication Table of Any Integer 
Date; 3rd october 2020
*/

#include <stdio.h>

/* STEPS;
- Declear the Integer [a]
- Print ' Enter the number ' 
- Take integer input from the user at the address of a
- Program
- Show the result as ' 3*1=3 '
- Print ' Thanks for coming ' 
*/

int main(int argc, char const *argv[])
{
    int a;
printf("Enter the number [a]\n");
scanf("%d", &a);
printf("\n");
printf("The Multiplication Table of %d\n", a);
printf("a*1= %d\n", a*1);
printf("a*2= %d\n", a*2);
printf("a*3= %d\n", a*3);
printf("a*4= %d\n", a*4);
printf("a*5= %d\n", a*5);
printf("a*6= %d\n", a*6);
printf("a*7= %d\n", a*7);
printf("a*8= %d\n", a*8);
printf("a*9= %d\n", a*9);
printf("a*10= %d\n", a*10);
printf("Thanks For Coming !\n");

    return 0;
}
