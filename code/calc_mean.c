#include <stdio.h>
#include <stdlib.h>


double mean(double a, double b) {
    return (a+b) / 2;
}


int main(int argc, char *argv[])
{
    int a = atoi(argv[1]);
    int b = atoi(argv[2]);
    printf("mean of %d, %d = %f", a, b, mean(a, b));
    return 0;
}
