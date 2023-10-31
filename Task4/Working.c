#include <stdio.h>

int main() {
    int n;
    printf("Enter the number of matrices you want to input: ");
    scanf("%d", &n);

    for (int k = 0; k < n; k++) {
        char matrix[3][3][50];  // Assuming each string has a maximum length of 50 characters

        printf("Enter elements for matrix #%d (3x3):\n", k + 1);

        // Input loop for a single 3x3 matrix
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                printf("Enter element at row %d, column %d: ", i + 1, j + 1);
                scanf("%s", matrix[i][j]);
            }
        }

        // Printing the matrix
        printf("Matrix #%d:\n", k + 1);
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                printf("%s ", matrix[i][j]);
            }
            printf("\n");
        }
    }

    return 0;
}
