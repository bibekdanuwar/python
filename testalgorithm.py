# n(i)(j): rows i=1..4, columns j=1..5
n = [[0]*6 for _ in range(5)]  # index 0 row/col unused, so we can use 1-based indices

# <入力値> - input values in order '10','20','30','40','50'
input_values = [10, 20, 30, 40, 50]

# Loop1: i = 1, j = 1 to 5 -> read input into row 1
i = 1
for j in range(1, 6):
    n[i][j] = input_values[j - 1]

# Loop2 (i=2..4) / Loop3 (j=1..5): n(i)(j) ← n(i-1)(j) + 5
for i in range(2, 5):
    for j in range(1, 6):
        n[i][j] = n[i - 1][j] + 5

# Loop4 (i=1..4) / Loop5 (j=1..5): n(i)(j) ← n(i)(j) + j
for i in range(1, 5):
    for j in range(1, 6):
        n[i][j] = n[i][j] + j

# Print the whole array to see how it evolved
for i in range(1, 5):
    print(f"n({i}):", [n[i][j] for j in range(1, 6)])

# Output ①: n(4)(5)
print("Output:", n[4][5])