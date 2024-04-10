#include <iostream>

int* add(int num1, int num2) {
    static int result = 0;
    result = num1 + num2;
    return &result;
}

int main() {
    std::cout << *add(9, 10) << std::endl;
    return 0;
}