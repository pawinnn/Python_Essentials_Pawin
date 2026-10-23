scores = []

for i in range(5):
    score = int(input(f"Enter score {i + 1}: "))
    scores.append(score)

total = sum(scores)
average = total / len(scores)
highest = max(scores)
lowest = min(scores)

print()
print(f"Total: {total}")
print(f"Average: {average:.2f}")
print(f"Highest: {highest}")
print(f"Lowest: {lowest}")
