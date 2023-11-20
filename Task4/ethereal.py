n = int(input("Enter the number of rows (n): "))
matrix = []

for i in range(n):
    row_input = input(f"Enter values for row {i + 1} (separated by space): ")
    row_values = list(map(int, row_input.split()))
    matrix.append(row_values)

# Display the matrix
print("Matrix:")
for row in matrix:
    print(row)

# Check column sums
for i in range(3):
    column_sum = sum(matrix[j][i] for j in range(n))
    if column_sum != 0:
        print("NO")
    else:
        print("YES")
