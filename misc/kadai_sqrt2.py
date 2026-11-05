import random

low = 1.0
high = 2.0

for i in range(50):
    mid = (low + high) / 2
    if mid * mid < 2:
        low = mid
    else:
        high = mid

print("二分探索法の結果:", mid)

count = 0

for i in range(1000000):
    x = random.uniform(0, 2)
    y = random.uniform(0, 2)
    if y >= x * x:
        count = count + 1

result = 3 * count / 1000000
print("モンテカルロ法の結果:", result)