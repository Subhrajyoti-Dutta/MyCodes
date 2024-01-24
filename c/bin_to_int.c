#include <stdio.h>

int main(){
    /*Start Your Code Here*/
    int input;
    int result, num1, num2;
    printf("Selct the number corresponding to the operation: \n\
    1. Addition\n\
    2. Subtraction\n\
    3. Multiplication\n\
    4. Division\n\
    Enter the number: ");
    num1 = 1;
    num2 = 2;
    scanf("%d",&input);
    switch(input){
        case 1:
        result = num1 + num2;
        break;
        case 2:
        result = num1 - num2;
        break;
        case 3:
        result = num1 * num2;
        break;
        case 4:
        result = num1 / num2;
        break;
    }
    printf("The result is : %d",result);
    return 0;
}