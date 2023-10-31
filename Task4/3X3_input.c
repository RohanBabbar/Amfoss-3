#include <stdio.h>

int main() {
    int matrix[3][3];

    // Input the matrix elements
    printf("Enter the elements of the 3x3 matrix:\n");
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            scanf("%d", &matrix[i][j]);
        }
    }

    // Check if any row has the same elements
    int found = 0;
    int day = 0;
    for (int i = 0; i < 3; i++) {
        int same = 1;  // Assume all elements in the row are the same
        for (int j = 1; j < 3; j++) {
            if (matrix[i][j] != matrix[i][0]) {
                same = 0;  // Not all elements in the row are the same
                break;
            }
           
        }
        if (same) {
            found = 1;
            printf("Row %d has the same elements.\n", i + 1);
        }
    }
    for (int j=0;j<3;j++){
        int not = 1;
        for (int i=1;i<3;i++){
            if (matrix[i][j] != matrix[0][j]){
                not = 0;
                break;
            }
        }
        if (not) {
            found = 1;
            printf("Column %d has the same elements.\n", j + 1);
        }
    }

    if (!found) {
        printf("No row has the same elements.\n");
    }

    return 0;
}
