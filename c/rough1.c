#include <stdio.h>


int main() {
    int a[3][3];
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            scanf("%d", &a[i][j]);
        }
    }
    for (int i = 0; i < 3; i++) {
        for (int j = i + 1; j < 3; j++) {
            // printf("%d %d %d %d %d %d \n", a[0][i] * a[1][j], a[0][i] * a[1][j], a[0][i] * a[2][j], a[2][i] * a[0][j], a[1][i] * a[2][j], a[2][i] * a[1][j]);
            if (a[0][i] * a[1][j] == a[1][i] * a[0][j] && a[0][i] * a[2][j] == a[2][i] * a[0][j] && a[1][i] * a[2][j] == a[2][i] * a[1][j]) {
                printf("%d#%d", i, j);
                return 0;
            }
        }

    }
    printf("0#0");
    return 0;
}