numbers = [52, 10, 31, 26, 8]
print("before sorting:", numbers)

for round_num in range(1, 6):
    for i in range(4):
        if numbers[i] > numbers[i + 1]:
            numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]

print(f"after round {round_num}: {numbers}")