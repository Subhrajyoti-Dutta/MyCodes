#include <stdio.h>
#include <math.h>

int main() {
    /*Start Your Code Here*/
    int num, rem;
    int res = 0;
    int i = 0;
    printf("Enter the decimal number: ");
    scanf("%d", &num);
    while (num > 0) {
        rem = num % 2;
        res += rem * (pow(10, i));
        num = num / 2;
        i++;
    }
    printf("%d", res);
    return 0;
}