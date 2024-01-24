#include <stdio.h>


int main() {
	int num;
	int prime = 1;
	printf("Enter Your Number: ");
	scanf("%d", &num);
	for (int i = 2; i < num / 2 + 1; i++) {
		if (num % i == 0) {
			prime = 0;
			break;
		}
	}
	if (prime) printf("%d is a prime number", num);
	else printf("%d is not a prime number", num);
	return 0;
}