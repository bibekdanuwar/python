# 1. assign the number 1 to variable count
count = 1

# 2. assign an empty list to variable scores
scores = []

# 3. create an infinite loop
while True:
    # 4. inside the loop, read user input, convert to int, and append to scores
    score_input = input(f"Enter score for test {count} => ")
    score = int(score_input)
    scores.append(score)

    # 5. ask whether to continue; if the user answers 'n' then break the loop
    retry = input("Enter another score? (y/n) => ")
    if retry == "n":
        break

    # advance to the next test number
    count += 1

# 6. compute the total from the scores list
total = 0
for score in scores:
    total += score

# 7. display the total
print("Total score: " + str(total))
