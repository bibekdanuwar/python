# Initialize the sum and the counter variable i
total_sum = 0
i = 1

# Loop continues until total_sum reaches 55
while total_sum < 55:
    total_sum += i
    print(f"Adding {i:2d} | Current Sum = {total_sum:2d}")
    i += 1

print("-" * 30)
print(f"Final Sum: {total_sum}")
print(f"Loop stopped at i = {i}")