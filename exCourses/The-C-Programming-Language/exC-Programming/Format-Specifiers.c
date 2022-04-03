
// Format Specifiers

#include <stdio.h>

int main(int argc, char const *argv[])

{

    printf("Format Specifiers\n");

    int a=3;

    float b=9.53;

    printf("the value of a is %d & value of b is %f\n", a, b);

    printf("%f\n", b);

    printf("%0.3f\n", b);

    printf("%10.2f\n", b);

    printf("%-15.4fblank space\n", b);

    printf("\n");

    printf("The numbers will be printed as per the code\n");

    return 0;

}
